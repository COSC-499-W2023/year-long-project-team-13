let camera_button = document.querySelector("#start-camera");
let video = document.querySelector("#video");
let start_button = document.querySelector("#start-record");
let stop_button = document.querySelector("#stop-record");
let download_link = document.querySelector("#download-video");
let videobox = document.querySelector('.video-box');
let next_button = document.querySelector("#next");
let side_bar_button = document.querySelector("#side-bar-btn");
let side_bar = document.querySelector("#mySidebar");

let camera_stream = null;
let media_recorder = null;
let blobs_recorded = [];

camera_button.addEventListener('click', async function() {
    camera_stream = await navigator.mediaDevices.getUserMedia({ video: true, audio: true });
    videobox.style.display = 'block';
    camera_button.style.display = 'none';
    start_button.style.display = 'block';
    video.srcObject = camera_stream;

});

start_button.addEventListener('click', function() {
    blobs_recorded = [];
    //add the stop button and remove the start button
    stop_button.style.display = 'block';
    start_button.style.display = 'none';
    // set MIME type of recording as video/webm
    media_recorder = new MediaRecorder(camera_stream, { mimeType: 'video/webm' });
    video.style.border = '10px solid red';

    // event : new recorded video blob available
    media_recorder.addEventListener('dataavailable', function(e) {
        blobs_recorded.push(e.data);
    });

    // event : recording stopped & all blobs sent
    media_recorder.addEventListener('stop', function() {
        let blob = new Blob(blobs_recorded, {type: "video/webm",}); // create blob from blobs_recorded

        let reader = new FileReader();  // read file

        reader.onloadend = function () {
            let base64data = reader.result.split(',')[1];
            document.getElementById('video_blob').value = base64data;   // store the video input value into form
        };

        reader.readAsDataURL(blob); // read the data of video, so can load it into mp4 file

        // create local object URL from the recorded video blobs
        //let video_local = URL.createObjectURL(new Blob(blobs_recorded, { type: 'video/webm' }));
        let video_local = URL.createObjectURL(blob);
        download_link.href = video_local;

        // remove stop button and add start button and download button and next button
        stop_button.style.display = 'none';
        start_button.style.display = 'block';
        download_link.style.display = 'block';
        next_button.style.display = 'block';
    });

    // start recording with each recorded blob having 1 second video
    media_recorder.start(1000);
});

stop_button.addEventListener('click', function() {
    media_recorder.stop();
    video.style.border = '2px solid black';
});

let detailsPage = document.querySelector('.detailsPage');
let previewPage = document.querySelector('.previewPage');
let back_record = document.querySelector('#back-record');
let back_details = document.querySelector('#back-details');
let submit_button = document.querySelector('#submit');
let preview_button = document.querySelector('#preview');
let submit_success = document.querySelector('.submit-success');
let title_input_id = document.querySelector('#title');
let title_input = "Title";
let description_input_id = document.querySelector('#description');
let description_input = "Description";
let contact_id = document.querySelector('#contact')
let contact_input = "contact"
let title_display = document.querySelector('#preview-title');
let description_display = document.querySelector('#preview-description');
let contact_display = document.querySelector('#preview-contact');
let video_display = document.querySelector('#vid-source');
let video_box = document.querySelector('#vid-box');
let horizontal_button = document.querySelector('#hor-button');

next_button.addEventListener('click', function() {
    detailsPage.style.display = 'block';
    start_button.style.display = 'none';
    stop_button.style.display = 'none';
    download_link.style.display = 'none';
    next_button.style.display = 'none';
    preview_button.style.display = 'block';
    back_record.style.display = 'block';
    videobox.style.display = 'none';
    side_bar_button.style.display = 'inline-block';
    side_bar.style.display = "block";

});

back_record.addEventListener('click', function() {
    detailsPage.style.display = 'none';
    start_button.style.display = 'block';
    stop_button.style.display = 'none';
    download_link.style.display = 'block';
    next_button.style.display = 'block';
    preview_button.style.display = 'none';
    back_record.style.display = 'none';
    videobox.style.display = 'block';
});

preview_button.addEventListener('click', function() {
    try {
        horizontal_button.style.marginTop = '20em';
        console.log("preview button clicked");
    } catch (e) {
        console.log(e);
    }
    previewPage.style.display = 'block';
    detailsPage.style.display = 'none';
    preview_button.style.display = 'none';
    submit_button.style.display = 'block';
    back_details.style.display = 'block';
    back_record.style.display = 'none';
    // get title, description, and contact inputed from user
    /*title_input = title_input_id.value;
    description_input = description_input_id.value;
    contact_input = contact_id.value;*/
    // display title, description, and contact username
    /*title_display.innerHTML = title_input;
    description_display.innerHTML = description_input;
    contact_display.innerHTML = "Request From: " + contact_input;*/

    // do an asynchronous update to show the video
    video_display.src = download_link.href;
    video_box.load();
    video_box.play();
});

back_details.addEventListener('click', function() {
    horizontal_button.style.marginTop = '0em';
    previewPage.style.display = 'none';
    detailsPage.style.display = 'block';
    preview_button.style.display = 'block';
    submit_button.style.display = 'none';
    back_details.style.display = 'none';
    back_record.style.display = 'block';
});

submit_button.addEventListener('click', function() {
    previewPage.style.display = 'none';
    detailsPage.style.display = 'block';
    start_button.style.display = 'none';
    stop_button.style.display = 'none';
    download_link.style.display = 'none';
    next_button.style.display = 'none';
    preview_button.style.display = 'block';
    submit_button.style.display = 'none';
    back_details.style.display = 'none';
    back_record.style.display = 'block';
    camera_button.style.display = 'none';
    videobox.style.display = 'none';
    submit_success.style.display = 'none';
    video.srcObject = null;
    camera_stream.getTracks().forEach(function(track) {
        track.stop();
    });
});
