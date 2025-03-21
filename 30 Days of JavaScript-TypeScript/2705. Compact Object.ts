/*
2705. Compact Object

Given an object or array obj, return a compact object.

A compact object is the same as the original object, except with keys containing falsy values removed. This operation applies to the object and any nested objects. Arrays are considered objects where the indices are keys. A value is considered falsy when Boolean(value) returns false.

You may assume the obj is the output of JSON.parse. In other words, it is valid JSON.

 

Example 1:

Input: obj = [null, 0, false, 1]
Output: [1]
Explanation: All falsy values have been removed from the array.
Example 2:

Input: obj = {"a": null, "b": [false, 1]}
Output: {"b": [1]}
Explanation: obj["a"] and obj["b"][0] had falsy values and were removed.
Example 3:

Input: obj = [null, 0, 5, [0], [false, 16]]
Output: [5, [], [16]]
Explanation: obj[0], obj[1], obj[3][0], and obj[4][0] were falsy and removed.
 

Constraints:

obj is a valid JSON object
2 <= JSON.stringify(obj).length <= 106
*/

type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function compactObject(obj: Obj): Obj {
    if (Array.isArray(obj)) {
        return obj.reduce((res: Array<JSONValue>, val: JSONValue) => {
            if (val) { // This will filter out falsy values, empty [] or {} are truthy
                if (Array.isArray(val) || typeof val === 'object') {
                    res.push(compactObject(val))
                } else { // If the value is a truthy literal-type, we push it back
                    res.push(val)
                }
            }
            return res;
        }, [])
    } else {
        return Object.keys(obj).reduce((res: Record<string, JSONValue>, key: string) => {
            const val = obj[key]
            if (val) {
                if (Array.isArray(val) || typeof(val) === 'object') {
                    res[key] = compactObject(val)
                } else {
                    res[key] = val
                }
            } 
            // if the value is falsy, we discard the value or the key entirely
            return res
        }, {})
    }
};