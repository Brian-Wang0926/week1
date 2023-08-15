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

// 取得會員資料
function getMember(){
    let username = document.querySelector("input[name='username']").value;
    fetch(`/api/member?username=${username}`)
    .then(function(res){
        return res.json();
    })
    .then(function(data){
        let memberInfo = document.getElementById("memberInfo")
        if (data.data !== null){
            memberInfo.textContent = `${data.name}(${data.username})`;
        }else{
            memberInfo.textContent = "無此會員"
        }
    })
    .catch(function(error){
        console.error("Fetch error:", error);
    });
}

// 更新會員名字
function rename(){
    let newName = document.querySelector("input[name='newName']").value;
    if(newName != ""){
        fetch("/api/member",{
            method: "PATCH",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({"name": newName})  //將物件轉為JSON
        })
        .then(function(res){
            return res.json();
        })
        .then(function(data){
            let renameInfo = document.getElementById("renameInfo");
            if(data.ok){
                renameInfo.textContent = "更新成功！";
            }else{
                renameInfo.textContent = "更新失敗！";
            }
        })
        .catch(function(error){
            console.error("Fetch error:", error);
        });
    }else{
        let renameInfo = document.getElementById("renameInfo");
        renameInfo.textContent = "請輸入新的姓名";
    }
}

