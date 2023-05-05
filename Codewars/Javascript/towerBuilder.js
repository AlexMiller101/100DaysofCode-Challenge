
function towerBuilder(nFloor){
    let tower = [];

    if(nFloor==1){
        tower.push("*");
        return tower;
    }
    if(nFloor<=0){
        return tower;
    }

    let space = " ";
    const star = "*";
    let r = "";
    total_space = (2*nFloor)-1;

    for(var n = 1; n<=nFloor; n++){
        r = "";
        let space_left = total_space - ((2*n)-1);
        let divider = space_left/2;

        for(var i = 1; i<=total_space-(Math.floor(total_space/2)); i++){
            if(i<=divider){
                r += space;
            }
            if(i>divider){
                r += star;
            }
            
        }

        let r2 = r.split("");
        r2 = r2.reverse();
        r2 = r2.slice(1).join("");
        r += r2;
        //console.log(r);
        tower.push(r);
    }
    return tower;
}

//towerBuilder(3);