
function count(string){
    let s = new Set(string);

    let sarray = Array.from(s);
    let count = 0;  
    let countjson = {};
    console.log(sarray);
    
    for(var i = 0; i<sarray.length; i++){
        for(var j = 0; j<string.length; j++){
            if(string[j] == sarray[i]){
                count += 1;
            }
        }
        countjson[sarray[i].toString()] = count;
        count = 0;
    }

    //console.log(count);
    console.log(countjson);
}

count("abacc");