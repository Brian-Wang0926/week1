// home.html
function validateForm(form){
    let inputs=form.getElementsByTagName("input");
    for (let i=0; i<inputs.length; i++){
        if(inputs[i].value.trim() === ""){
            alert("請輸入完整資料！");
            return false;
        }
    }
    return true;
}

// success.html
function confirmDelete(form,messageId){
    if(!confirm("確定要刪除這則訊息嗎？")){
        return false;
    }
    form.submit();
}