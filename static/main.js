function copy_to_clipboard() {
    let buttons = document.querySelectorAll('.clipboard');
    for (let button of buttons) {
        button.addEventListener('click', function (e) {
            let parent = e.target.closest('.code-snippet')
            let snippet = parent.querySelector('code')
            let range = document.createRange()
            range.selectNode(snippet)
            window.getSelection().removeAllRanges()
            window.getSelection().addRange(range)
            try {
                let successful = document.execCommand('copy')
                let msg = successful ? 'successful' : 'unsuccessful'
            } catch (err) {
                console.log('Sorry, unable to copy snippet')
            } window.getSelection().removeAllRanges()
        })
    }
}

function main() {
    copy_to_clipboard()
}

document.addEventListener('DOMContentLoaded', function () {
    main()
})



//code-snippet and codearea

// function copy_to_clipboard() {
//     let buttons = document.querySelectorAll('.fa-clipboard');
//     for (let button of buttons) {
//         button.addEventListener('click', function(event) {
//             let parent = event.target.closest('.code-snippet');
//             let snippet = parent.querySelector('code');
//             let range = document.createRange();
//             range.selectNode(snippet);
//             window.getSelection().removeAllRanges();
//             window.getSelection().addRange(range);
//             try {
//                 let successful = document.execCommand('copy');
//                 let msg = successful ? 'successful' : 'unsuccessful';
//                 console.log('Copy snippet command was ' + msg);
//             } catch(err) {
//                 console.log('Sorry, unable to copy snippet');
//             } window.getSelection().removeAllRanges();
//         })
//     }   
// }




// function q(selector) {
//     return document.querySelector(selector)
// }


// function copyToClipboard() {
//     let clipboardButton = q("#clipboard")
//     let str = document.getElementById("#codearea").innerText
//     clipboardButton.addEventListener("click", function (event) {
//         event.preventDefault
//         const copyToClipboard = str => {
//             const el = document.createElement('textarea')
//             el.value = str
//             el.setAttribute('readonly', '')
//             el.style.position = 'absolute'
//             // el.style.left = '-9999px'
//             document.body.appendChild(el)
//             // const selected = document.getSelection().rangeCount > 0 ? document.getSelection().getRangeAt(0) : false
//             // el.select()
//             document.execCommand('copy')
//             // document.body.removeChild(el)
//             // if (selected) {
//             //     document.getSelection().removeAllRanges()
//             //     document.getSelection().addRange(selected)
//             // }
//         }
//     })
// }




