
document.addEventListener('DOMContentLoaded', function (e) {
    console.log('DOM ARE LOADED');

    let btn = document.getElementById('phone-reset'),
        input = document.getElementById('user_phone'),
        mod = document.getElementById('userAuth');

    document.getElementById('formMod').addEventListener('submit', (e) => {
        e.preventDefault();
        onSubmitPost('https://unistock.online', {"phone": input.value})
            .then(
                (data) => {
                    let invalid = document.querySelector(
                        '.invalid-feedback');

                    btn.classList.add('hidden');
                    invalid.textContent = `${data.phone}`;
                    document.forms[0].reset();
                    input.classList.add('is-invalid');
            })
    })

    btn.addEventListener( 'click', () => {
        document.forms[0].reset();
    });

    input.addEventListener('focusin', (e) => {
        e.preventDefault();
        if (input.className.match('is-invalid')) {
            input.classList.remove('is-invalid');
        }
        if (input.value.length === 0) input.value = '+7';
        btn.classList.remove('hidden');
    })

    // input.addEventListener('change', () => {
    //
    //     if (input.value === '+7') document.forms[0].reset();
    //
    //     btn.classList.add('hidden');
    // })

    mod.addEventListener('hide.bs.modal', () => {

    })

    mod.addEventListener('shown.bs.modal', () => {
        input.focus();
    })

    input.addEventListener('keyup', onInput);

})

function onInput(e) {
    let inp = e.currentTarget;


    if (e.key !== 'Backspace' && inp.value.slice(0, 2) !== '+7') {
        inp.value = '+7'.concat(inp.value);
    }

    if (e.key !== 'Backspace' &&
        e.key !== 'ArrowLeft' &&
        e.key !== 'ArrowRight' &&
        inp.selectionStart === 5 &&
        inp.selectionStart === inp.value.length) {
        inp.value = inp.value.slice(0, 2).concat('(', inp.value.slice(2, 5), ')')
    }

    if (e.key !== 'Backspace' &&
        e.key !== 'ArrowLeft' &&
        e.key !== 'ArrowRight' &&
        (inp.selectionStart === 8 || inp.selectionStart === 12||
            inp.selectionStart === 15)) {
        let arr = Array.from(inp.value);
        arr.splice(inp.selectionStart - 1, 0, '-');
        inp.value = arr.join('');
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

async function onSubmitPost(url="", data={}) {
    const response = await fetch(url, {
        method: "POST",
        credentials: "same-origin",
        headers: {
            "Accept": "application/json",
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify(data)
    })
    return await response.json();
    // if (response.ok) {
    //     let result = response.json();
    //     alert(result);
    // } else {
    //     alert(response.status);
    // }
}














