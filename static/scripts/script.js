console.log('Hello world');
// const uploadWrapper = document.querySelector('.uploadUnderlay');
const closeUpload = document.querySelector('.closeUploadBtn');
const openUpload = document.querySelector('#uploadBtn');
const site = document.querySelector('.site');

openUpload.addEventListener('click', ()=> {
      site.classList.add('showUpload');
});

closeUpload.addEventListener('click', ()=> {
      site.classList.remove('showUpload');
});


const form = document.getElementById('upload-form'); 
// console.log(form);
const fileInput = form.querySelector('.file-input');
const progressArea = document.querySelector('.progress-area'); 
const uploadedArea = document.querySelector('.uploaded-area'); 

const csrf = document.getElementsByName('csrfmiddlewaretoken');

// console.log(csrf[0].value);


console.log(fileInput);
form.addEventListener('click', ()=>{
      fileInput.click();
});

fileInput.onchange = ({target}) =>{
      let file = target.files[0];
      // console.log(file);

      const  formData = new FormData();
      formData.append('csrfmiddlewaretoken', csrf[0].value);
      formData.append('video', file);
      // console.log(formData);
      if(file){
            let filename = file.name;
            if(filename.length >= 12){
                  let splitName = filename.split('.');
                  filename = splitName[0].substring(0, 12) + '... .' + splitName[1];
            }
            $.ajax({
                  type: 'POST',
                  url: form.action,
                  enctype : 'multipart/form-data',
                  data: formData,
                  beforeSend: function(){

                  },
                  xhr: function(){
                        const xhr = new window.XMLHttpRequest()
                        xhr.upload.addEventListener('progress', ({loaded, total}) => {
                              let fileloaded = Math.floor((loaded / total) * 100);
                              let fileTotal = Math.floor(total / 1000);
                              let fileSize;
                              (fileTotal < 1024) ? fileSize = fileTotal + 'KB' : fileSize = (loaded / (1024 * 1024).toFixed(2)) + ' MB';
                              let progressHTML = `<li class="row">
                                                      <i class="ri-file-text-fill"></i>
                                                      <div class="content">
                                                            <div class="details">
                                                                  <span class="name">${filename} • Uploading</span>
                                                                  <span class="percent">${fileloaded} %</span>
                                                            </div>
                                                            <div class="progress-bar">
                                                                  <div class="progress" style="width: ${fileloaded}%"></div>
                                                            </div>
                                                      </div>
                                                </li>`;
                              uploadedArea.innerHTML = '';
                              progressArea.innerHTML = progressHTML;

                              if(loaded == total){
                                    progressArea.innerHTML = '';
                                    let uploadedHTML = `<li class="row">
                                                            <div class="content">
                                                                  <i class="ri-file-text-fill"></i>
                                                                  <div class="details">
                                                                        <span class="name">${filename} • Uploaded</span>
                                                                        <span class="size">${fileSize}</span>
                                                                  </div>
                                                            </div>
                                                            <i class="ri-check-line"></i>
                                                      </li>`;
                                    uploadedArea.innerHTML = uploadedHTML;
                              }
                        });

                        return xhr
                  },

                  success: function(response){
                        console.log(response)
                  },

                  error: function(error){
                        console.log(error)
                  },
                  Cache : false,
                  contentType : false,
                  processData: false,

            });
      }

}
