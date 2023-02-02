const mod = document.getElementById('userAuth');

mod.addEventListener('show.bs.modal', event => {
    const btn = mod.querySelector('.authForm button'),
          form = document.forms[0];

    btn.onclick = () => {
        form.reset();
        mod.querySelector('.invalid').classList.remove('hidden');
        form.phone.onclick = () => {
            mod.querySelector('.invalid').classList.add('hidden');
        }
    }
})

mod.addEventListener('hidden.bs.modal', event => {
    mod.querySelector('.invalid').classList.add('hidden');
})
