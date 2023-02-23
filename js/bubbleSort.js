var sequence = [4, 3, 5, 0, 1]
var swaps = 0

// Your Code Here
function result (numberList) {
    let isSwapped = true
    while (isSwapped) {
        isSwapped = false
        for (let i = 0; i < numberList.length; i++){
            let prev = numberList[i]
            let curr = numberList[i+1]
            if (numberList[i] > numberList[i+1]){
                numberList[i] = curr
                numberList[i+1] = prev
                isSwapped = true
                swaps ++
            }
        }
    }
    return numberList
}



console.log("Final result: " + result(sequence))
console.log("Swaps: " + swaps)
