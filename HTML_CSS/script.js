document.addEventListener('DOMContentLoaded', () => {
    const sideBar = document.getElementById('side-bar');
    const openBtn = document.getElementById('open-btn');
    const closeBtn = sideBar.querySelector('ion-icon[name="close"]');
    const home = document.getElementById('home');
    const voiceRecordBtn = document.getElementById('voice-record-btn');
    const audioVisualizer = document.getElementById('audio-visualizer');
    const timer = document.getElementById('timer');
    let audioContext, analyser, microphone, javascriptNode;
    let recording = false;
    let startTime;

    openBtn.addEventListener('click', () => {
        sideBar.classList.add('open');
        home.style.width = '75%'; // Ajuster la largeur de la div home lorsque le side-bar est ouvert
    });

    closeBtn.addEventListener('click', () => {
        sideBar.classList.remove('open');
        home.style.width = '100%'; // Rétablir la largeur de la div home lorsque le side-bar est fermé
    });

    voiceRecordBtn.addEventListener('click', () => {
        if (!recording) {
            startRecording();
        } else {
            stopRecording();
        }
    });

    function startRecording() {
        recording = true;
        voiceRecordBtn.classList.add('active');
        startTime = new Date();
        timerInterval = setInterval(updateTimer, 1000);

        if (!audioContext) {
            audioContext = new (window.AudioContext || window.webkitAudioContext)();
        }

        navigator.mediaDevices.getUserMedia({ audio: true })
            .then(stream => {
                microphone = audioContext.createMediaStreamSource(stream);
                analyser = audioContext.createAnalyser();
                javascriptNode = audioContext.createScriptProcessor(2048, 1, 1);

                analyser.smoothingTimeConstant = 0.3;
                analyser.fftSize = 1024;

                microphone.connect(analyser);
                analyser.connect(javascriptNode);
                javascriptNode.connect(audioContext.destination);

                javascriptNode.onaudioprocess = () => {
                    const array = new Uint8Array(analyser.frequencyBinCount);
                    analyser.getByteFrequencyData(array);
                    drawVisualizer(array);
                };
            })
            .catch(err => console.error('Error accessing microphone: ', err));
    }

    function stopRecording() {
        recording = false;
        voiceRecordBtn.classList.remove('active');
        clearInterval(timerInterval);
        timer.textContent = '00:00';
        if (microphone) microphone.disconnect();
        if (analyser) analyser.disconnect();
        if (javascriptNode) javascriptNode.disconnect();
    }

    function updateTimer() {
        const now = new Date();
        const elapsed = Math.floor((now - startTime) / 1000);
        const minutes = String(Math.floor(elapsed / 60)).padStart(2, '0');
        const seconds = String(elapsed % 60).padStart(2, '0');
        timer.textContent = `${minutes}:${seconds}`;
    }

    function drawVisualizer(array) {
        const canvas = audioVisualizer;
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        const width = canvas.width;
        const height = canvas.height;
        const barWidth = width / array.length;

        for (let i = 0; i < array.length; i++) {
            const value = array[i];
            const percent = value / 256;
            const barHeight = height * percent;
            const offset = height - barHeight - 1;

            ctx.fillStyle = `red`; // Change to red color for all bars
            ctx.fillRect(i * barWidth, offset, barWidth, barHeight);
        }
    }
});
