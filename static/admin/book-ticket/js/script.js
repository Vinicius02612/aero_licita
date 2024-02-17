let person_passenger = {
    'first_name': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
    },
    'last_name': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
    },
    'cpf': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
        'mask': '000.000.000-00',
    },
    'rg': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
        'mask': '',
    },
    'birthday': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
    },
    'email': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,

    },
    'phone': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
        'mask': '(00) 00000-0000'
    },
    'special': {
        'value': 'nao',
        'error': false,
        'error_msg': '',
        'required': true,
    },
}

let company_passenger = {
    'first_name_company': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
    },
    'last_name_company': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
    },
    'cnpj': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
        'mask': '00.000.000/0000-00',
    },
    'business_name': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
    },
    'phone_company': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
        'mask': '(00) 00000-0000'
    },
    'special_company': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
    },
    'fantasy_name': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
    },
    'birthday_company': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
    },
}
let payer_data = {
    'first_name_payer': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
    },
    'last_name_payer': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
    },
    'cpf_payer': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
        'mask': '000.000.000-00',
    },
    'email_payer': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
    },
    'cep_payer': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
        'mask': '00000-000',
    },
}
let payment_data = {
    'payment-type': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': false,
    },
    'payment-type1': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': false,
    },
    'card_number': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
        'mask': '0000 0000 0000 0000',
    },
    'card_name': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
    },
    'card_date': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
    },
    'card_cvv': {
        'value': '',
        'error': false,
        'error_msg': '',
        'required': true,
        'mask': '000',
    },
}
let forms = {
    'passenger_form': '',
    // 'special_form': '',
    'payer_form': '',
    'payment_form': '',
}
let radios = document.getElementsByName("passenger-type");

let add_ev = (radio) => {
    radio.addEventListener('change', () => {
        let forms = document.querySelectorAll('.passenger-infos-docs');
        let juridica = forms[1];
        let fisica = forms[0];
        switch (radio.value) {
            case 'juridica':
                juridica.classList.add('active');
                juridica.classList.remove('hidden');
                juridica.classList.add('passenger-active');

                fisica.classList.remove('active');
                fisica.classList.remove('passenger-active');
                fisica.classList.add('hidden');
                break;
            case 'fisica':
                fisica.classList.add('active');
                fisica.classList.remove('hidden');
                fisica.classList.add('passenger-active');

                juridica.classList.remove('active');
                juridica.classList.remove('passenger-active');
                juridica.classList.add('hidden');
                break;
            default:
                break;
        }
    })
}

radios.forEach(radio => add_ev(radio));

let getValue = (input, id, obj) => {
    input.addEventListener('change', (e) => {
        let value = e.target.value;
        obj[id].value = value;
    })
}

let getForm = (id) => {
    let classList = document.getElementById(id).classList;
    forms[id] = classList;
}

for (let key in forms) {
    getForm(key);
}

let initForms = (forms) => {
    for (let form in forms) {
        for (let key in forms[form]) {
            let input = document.getElementById(key);
            if (forms[form][key]?.mask != '' && forms[form][key]?.mask != undefined) {
                IMask(input, { 'mask': forms[form][key].mask });
            }
            getValue(input, key, forms[form]);
        }
    }
}

initForms([person_passenger, company_passenger, payer_data, payment_data]);

let addError = (id, obj, error) => {
    obj[id].error = true;
    obj[id].error_msg = 'Campo obrigatório';
}

let verifyForm = () => {
    let flag = true;
    let forms = [person_passenger, company_passenger, payer_data, payment_data]
    for (let form in forms) {
        for (let key in forms[form]) {
            if (forms[form][key].required == true && forms[form][key].value == '') {
                addError(key, forms[form], "Campo obrigatório");
                flag = false;
            }
        }
    }

    return flag;

}

document.querySelector(".confirm").addEventListener("click", () => {
    let flag = false;
    for (let key in forms) {
        if (flag == true) {
            document.getElementById(key).classList.add('form-active');
            document.getElementById(key).classList.remove('form-hidden');
            document.querySelector('.' + key).classList.add('passed');
            flag = false;
            break;
        }
        if (forms[key].contains('form-active') && key != 'payment_form') {
            document.getElementById(key).classList.add('form-hidden');
            document.getElementById(key).classList.remove('form-active');
            flag = true;
        }
        if (forms[key].contains('form-active') && key == 'payment_form') {
            flag = true;
        }
    }
    if (flag == true) {
        //Enviar formulários;
        let verify = verifyForm();
        if (verify == true) {
            let forms = [person_passenger, company_passenger, payer_data, payment_data]
            let data = {};
            for (let form in forms) {
                for (let key in forms[form]) {
                    data[key] = forms[form][key].value;
                }
            }
            console.log(data);
            // fetch('http://
        } else {
            let forms = [person_passenger, company_passenger, payer_data, payment_data]
            for (let form in forms) {
                for (let key in forms[form]) {
                    if (forms[form][key].error == true) {
                        let input = document.getElementById(key);
                        let parent = input.parentNode;
                        let error = document.createElement('p');
                        error.classList.add('text-red');
                        error.innerHTML = forms[form][key].error_msg;
                        parent.appendChild(error);
                    }
                }
            }
            alert('Preencha todos os campos');
        }

    }
    for (let key in forms) {
        getForm(key);
    }
})

document.querySelector(".back-form").addEventListener("click", () => {
    let flag = false;
    let newForm = [];
    for (let key in forms) {
        newForm.push([key, forms[key]])
    }
    newForm = newForm.reverse();
    for (let key in newForm) {
        if (flag == true) {
            document.getElementById(newForm[key][0]).classList.add('form-active');
            document.getElementById(newForm[key][0]).classList.remove('form-hidden');
            flag = false;
            break
        }
        if (newForm[key][1].contains('form-active') && key != newForm.length - 1) {
            document.getElementById(newForm[key][0]).classList.add('form-hidden');
            document.getElementById(newForm[key][0]).classList.remove('form-active');
            document.querySelector('.' + newForm[key][0]).classList.remove('passed');
            flag = true;
        }
    }
    for (let key in forms) {
        getForm(key);
    }
})