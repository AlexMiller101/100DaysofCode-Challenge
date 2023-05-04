

function longest(s1, s2){
    let s1array = s1.split("");
    let s2array = s2.split("");

    let sumarray = s1array.concat(s2array);
    
    let longestSet = new Set(sumarray);
    let longestarray = Array.from(longestSet).sort();
    let longest = longestarray.join("");
    return longest;
}

longest("xyaabbbccccdefww", "xxxxyyyyabklmopq");