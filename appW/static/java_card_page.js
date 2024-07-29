const body_memes = document.getElementById('geter_area');
const newMbtn = document.getElementById('btnNmem');
const search_odId_btn = document.getElementById('_getmemes');
const cards_AREA = document.getElementById('CONTENT_CARDS_AREA')

search_odId_btn.addEventListener('click', function() {
    const search_onId = document.getElementById('Id_pole_search').value;
    if (search_onId === '') {
        location.reload(100);
        return;
    }
    id_search_and_del_cards(search_onId);

})

function id_search_and_del_cards(search_onId) {
    var Image_card__i__i = document.getElementById('#id_card__'+search_onId);
    $('.content_area_dinamic').children().not('#id_card__'+search_onId).hide();
    $('.content_area_dinamic').children('#id_card__'+search_onId).show();
}

function printer_cards_in_DB(db_data){
    for (var  lister in db_data){
        var jsonser = db_data[lister]
        var id = jsonser['id']
        var name = jsonser['name']
        var des_ = jsonser['des_']
        var Img_id = '/imGG/'+ jsonser['Img_id']
        create_card_meme(id, name, Img_id, des_)
        console.log('|create_init|')
    }
}

function prewImage(file) {
    const reader = new FileReader();
    reader.onload = () => document.getElementById("img__").src = reader.result;
    reader.readAsDataURL(file);
}

newMbtn.addEventListener('click', function() {
    const create_area = document.getElementById('inp_geter_area');
    console.log(create_area)
    if (create_area == null){
        add_memes_action_area();
    } else {
        body_memes.removeChild(create_area);
    }
});
function Fgetter_area() {
    const form = document.createElement('form');
    form.setAttribute('class', 'Getter_area_memes');
    form.setAttribute('id', 'Id_My_form');
    form.setAttribute('method', 'post');
    /*form.setAttribute('action', 'memes');*/

    const getter_area = document.createElement('div');
    getter_area.setAttribute('class', 'Getter_area_memes');
    getter_area.setAttribute('id', 'inp_geter_area');
    getter_area.style.zIndex = '1000';

    form.appendChild(getter_area);
    return getter_area;
}
function add_memes_exit_btn() {
    const getter_exit = document.createElement('div');
    const exit_h4 = document.createElement('h4');
    exit_h4.textContent = 'exit'
    getter_exit.setAttribute('class', 'create_area cre_ext');
    getter_exit.appendChild(exit_h4);
    return getter_exit;

}
function Fun_img_area(Img_new_) {
    const img_area = document.createElement('div');

    const area_image = document.createElement('div');
    const img_inP = document.createElement('input');
    const Image_item = document.createElement('img');
    if (Img_new_ != undefined) {
        Image_item.src = Img_new_;
    }


    img_area.setAttribute('class', 'getter_area_el padderImage');

    area_image.setAttribute('id', 'AREA_img');
    area_image.style.marginTop = '10%';

    img_inP.setAttribute('id', '__Image_input');
    img_inP.setAttribute('oninput', 'prewImage(this.files[0])')
    /*img_inP.setAttribute('accept', 'image/*');*/
    img_inP.setAttribute('type', 'file');
    img_inP.setAttribute('name', 'Img_input');

    Image_item.setAttribute('id', 'img__');

    area_image.appendChild(Image_item);
    img_area.appendChild(img_inP);
    img_area.appendChild(area_image);
    return img_area;
}
function add_memes_action_area(Id_, Name_new_, Img_new_, desc_new_) {
    const getter_area = Fgetter_area()
    if (Id_ != undefined) {
        const Id_upgraded = document.createElement('div');
        Id_upgraded.setAttribute('id', 'id_upgraded')
        const txtId = document.createElement('h3');
        txtId.textContent = "Мем UPD// \nId:"+Id_;
        Id_upgraded.appendChild(txtId);
        getter_area.appendChild(Id_upgraded);
    }
    getter_exit = add_memes_exit_btn()

    const name_area = document.createElement('textarea');
    name_area.setAttribute('maxlength', '100');
    if (Name_new_ != undefined) {
        name_area.textContent = Name_new_;
    }
    const img_area = Fun_img_area(Img_new_)
    const descr_area = document.createElement('textarea');
    if (desc_new_ != undefined) {
        descr_area.textContent = desc_new_;
    }
    const create_button = document.createElement('input');

    const create_h2 = document.createElement('h2');

    create_h2.style.margin = '1%';
    create_h2.textContent = 'CREATE MEME';

    name_area.setAttribute('class', 'getter_area_el');
    name_area.setAttribute('id', 'are_v1');
    name_area.setAttribute('placeholder', 'Name');
    name_area.setAttribute('name', 'Name_areas');

    descr_area.setAttribute('class','getter_area_el are_V2');
    descr_area.setAttribute('id', 'Id_new_descript');
    descr_area.setAttribute('name', 'descriptionses');
    descr_area.setAttribute('placeholder', 'DESCRIPT');
    create_button.setAttribute('class', 'create_area clt');
    create_button.setAttribute('id', '__btn_create');
    create_button.setAttribute('type', 'submit');
    create_button.setAttribute('value', 'submit');

    create_button.appendChild(create_h2);
    getter_area.appendChild(getter_exit);

    getter_area.appendChild(name_area);
    getter_area.appendChild(img_area);
    getter_area.appendChild(descr_area);
    getter_area.appendChild(create_button);

    body_memes.appendChild(getter_area);

    getter_exit.addEventListener('click', function() {
        setTimeout(400);
        body_memes.removeChild(getter_area);
        return;
    })
    create_button.addEventListener('click', function(event){
        event.preventDefault();
        const Name_new = document.getElementById('are_v1').value;
        const Img_new = document.getElementById('img__').src;
        const desc_new = document.getElementById('Id_new_descript').value;
        if (Name_new ==='') {
            alert('Поле названия не может быть пустым!');
            return;
        } else if (desc_new ===''){
            alert('Описание должно быть!');
            return;
        } else if (Img_new === '') {
            alert('Изображение Пжалста!');
            return;
        }
        const FILE_IMG = document.getElementById('__Image_input');
        if (FILE_IMG.files[0]) {
            var datas = new FormData();
            datas.append('users_rev',  JSON.stringify({'name': Name_new, 'descr': desc_new, 'imgDel': Img_new_}));
            datas.append('image', FILE_IMG.files[0]);
            if (Id_ != undefined){
                console.log(Img_new_)
                fetch('memes/' + Id_, {
                    method:'PUT',
                    headers: {
                        'Accept': 'application/json'
                    },
                    body: datas
                })
                .then(resp => resp.text())
                .then(data => {
                document.getElementById('responseArea').innerHTML;
                })
                .catch(error => {
                    console.error(error);
                })
                alert('Мем Обновлён!')
                location.reload();
                return;
            }

            datas.append('users_rev',  JSON.stringify({'name': Name_new, 'descr': desc_new}));
            datas.append('image', FILE_IMG.files[0]);
            fetch('memes', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json'
                },
                body: datas
            })
            .then(resp => resp.text())
            .then(data => {
                document.getElementById('responseArea').innerHTML;
            })
            .catch(error => {
                console.error(error);
            })
        } else {
            alert('Изображение тоже должно быть обновлено!')
            return;
        }
        const Id='None'
        create_card_meme(Id, Name_new, Img_new, desc_new)
        alert('Мем создан!')
        location.reload()
    })
}

function C_card(id) {
    const card = document.createElement('div');
    card.setAttribute('class', 'content_card');
    card.setAttribute('id', 'id_card__'+id)
    return card;
}
function C_name(Nm){
    const name = document.createElement('p');
    name.setAttribute('class', 'name');
    name.textContent = Nm;
    return name;
}
function C_Id(id){
    const Id = document.createElement('h5');
    Id.textContent = '#ID: |>' + id;
    Id.setAttribute('id', 'Id_Card__'+id)
    return Id;
}
function C_content(){
    const content = document.createElement('div');
    content.setAttribute('class', 'content_');
    return content;
}
function C_separator(){
    const __separator__ = document.createElement('div');
    __separator__.setAttribute('class', 'bb_deso');
    return __separator__;

}
function C_Image(img){
    const image = document.createElement('div');
    if (img === '') {
       console.log('Image None');
    } else {
        const img_teg = document.createElement('img');
        img_teg.setAttribute('class', 'obg IMG_hover');
        img_teg.src = img;
        img_teg.style.position = 'relative';
        image.style.boxShadow = '0px 10px 20px 2px rgba(0, 0, 0, 0.25)';
        image.appendChild(img_teg);
    }

    image.setAttribute('class', 'content_image');
    return image;
}
function C_descript(des){
    const descript = document.createElement('div');
    const textd = document.createElement('p');
    textd.textContent = des;
    descript.setAttribute('class', 'content_descript');
    descript.appendChild(textd);
    return descript;

}
function C_buttons(){
    const buttons = document.createElement('div');
    buttons.setAttribute('class', 'content_buttons');
    return buttons;
}
function C_btn_up(id){
    const btn = document.createElement('button');
    btn.setAttribute('class', 'btn_icon');

    const btn_up = document.createElement('img');
    btn_up.setAttribute("src", '/icons/update.ico')
    btn_up.setAttribute('class', 'btn_Img_');

    btn.appendChild(btn_up);
    return btn;
}
function C_btn_search(Id_){
    const btn = document.createElement('button');
    btn.setAttribute('class', 'btn_icon');


    const btn_search = document.createElement('img');
    btn_search.setAttribute("src", '/icons/select.ico')
    btn_search.setAttribute('class', 'btn_Img_');
    btn.appendChild(btn_search)

    const btnhref = document.createElement('a');
    btnhref.setAttribute('href', '/Operatro/memes/'+Id_)
    btnhref.appendChild(btn)

    return btnhref;
}
function C_btn_delete(){
    const btn = document.createElement('button');
    btn.setAttribute('class', 'btn_icon');

    const btn_delete = document.createElement('img');
    btn_delete.setAttribute("src", '/icons/delete.ico')
    btn_delete.setAttribute('class', 'btn_Img_');

    btn.appendChild(btn_delete);
    return btn;
}
function create_card_meme(Id_, Name_new_, Img_new_, desc_new_) {
    const card = C_card(Id_);
    const name = C_name(Name_new_);
    const Id = C_Id(Id_);

    const content = C_content();
    const __separator__1 = C_separator();
    const __separator__2 = C_separator();
    const __separator__3 = C_separator();


    const image = C_Image(Img_new_);
    const descript = C_descript(desc_new_);
    const buttons = C_buttons();

    const btn_up = C_btn_up(Id_);
    const btn_search = C_btn_search(Id_);
    const btn_delete = C_btn_delete();

    buttons.appendChild(btn_search);
    buttons.appendChild(btn_up);
    buttons.appendChild(btn_delete);

    content.appendChild(__separator__1);
    content.appendChild(image);
    content.appendChild(descript);
    content.appendChild(__separator__2);
    content.appendChild(buttons);
    card.appendChild(name);
    card.appendChild(Id);
    card.appendChild(content);
    content.appendChild(__separator__3);

    cards_AREA.appendChild(card);

    btn_up.addEventListener('click', function() {
        add_memes_action_area(Id_, Name_new_, Img_new_, desc_new_)
    })
    btn_delete.addEventListener('click', function() {
        alert('Карта удалена...');
        cards_AREA.removeChild(card);
        fetch('memes/'+Id_, {
            method: 'DELETE'
        })
    })
}