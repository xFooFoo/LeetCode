type F = (x: number) => number;

function compose(functions: F[]): F {
        if (functions.length === 0) {
            return (x: any) => x;
        }
        return functions.reduceRight((function_comp, curr_function) => {
            return (x: number) => curr_function(function_comp(x))
        }, (x: number) => x)
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */