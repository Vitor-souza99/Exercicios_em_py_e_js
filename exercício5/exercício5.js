function inverterString() {
    let inputString = document.getElementById("inputString").value;
    let outputString = "";
  
    for (let i = inputString.length - 1; i >= 0; i--) {
      outputString += inputString[i];
    }
  
    document.getElementById("resultado").innerHTML = outputString;
  }
  