type ToBeOrNotToBe = {
    toBe: (val: any) => boolean;
    notToBe: (val: any) => boolean;
};

function expect(val: any): ToBeOrNotToBe {
    function toBe(anotherVal: any): boolean {
        if (val === anotherVal) { return true}
        else {throw new Error("Not Equal")}
    }
    function notToBe(anotherVal: any): boolean {
        if (val !== anotherVal) { return true}
        else {throw new Error("Equal")}
    }

    return {
        toBe,
        notToBe
    };
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */