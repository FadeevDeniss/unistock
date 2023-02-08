window.addEventListener('load', (e) => {
    const input = document.getElementById('user_phone');

    input.addEventListener('focusin', () => {
        if (input.value.length === 0) input.value = '+7';
    })

    input.addEventListener('focusout', () => {
        if (input.value.length < 3) {
            input.value = '';
        }

    })

    input.addEventListener('keyup', (e) => {

        if (e.key !== 'Backspace' && input.value.length === 3) {
            input.value = input.value.replace('+7', '+7(');
        }

        if (e.key !== 'Backspace' && input.value.length === 6) {
            input.value += ')';
        }

        if (e.key !== 'Backspace' && (
            input.value.length === 7 ||
            input.value.length === 11 ||
            input.value.length === 14
        )) {
            input.value += '-';
        }
    })
})










