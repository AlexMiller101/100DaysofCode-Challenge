
// Take arrays of numbers and return a string in phone number format

const extractCountryCode = function(numbers){
    let countryCodelist = numbers.slice(0,3);
    let countryCode = "(";
    countryCodelist.forEach(a => {
        countryCode += a;
    });
    countryCode += ")";
    return countryCode;
}

const extractThreeCode = function(numbers){
    let threeCodeList = numbers.slice(3,6);

    let threeCode = " ";
    threeCodeList.forEach(b => {
        threeCode += b;
    });
    threeCode += "-";
    return threeCode;
}

const extractLastCode = function(numbers){
    let lastCodeList = numbers.slice(6,10);

    let lastCode = "";
    lastCodeList.forEach(c => {
        lastCode += c;
    });
    return lastCode;
}

function createPhoneNumber(numbers){
    let countryCode = extractCountryCode(numbers);
    let threeCode = extractThreeCode(numbers);
    let lastCode = extractLastCode(numbers);

    let phoneNumber = "";
    phoneNumber += countryCode + threeCode + lastCode;
    return phoneNumber;
}
