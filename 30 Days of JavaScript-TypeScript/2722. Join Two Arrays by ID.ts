type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type ArrayType = { "id": number } & Record<string, JSONValue>;

function join(arr1: ArrayType[], arr2: ArrayType[]): ArrayType[] {
    const map = new Map<number, ArrayType>();
    // Map arr2 objects to their id for faster lookups
    arr2.forEach(obj => map.set(obj.id, obj))

    arr1.forEach((obj1) => {
        const existingObj = map.get(obj1.id);
        // same object id so we merge
        if (existingObj) {
            for (const key in obj1) {
                if (!existingObj.hasOwnProperty(key)) {
                    existingObj[key] = obj1[key];
                }
            }
        } else {
            // arr2 doesn't have an obj with same id
            map.set(obj1.id, obj1)
        }
    })
    const result = Array.from(map.values());
    return result.sort((obj1, obj2) => obj1.id - obj2.id);
};