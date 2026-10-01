const output = document.getElementById("output");
const startButton = document.getElementById("startButton");

const SpeechRecognition =
    window.SpeechRecognition || window.webkitSpeechRecognition;

if (!SpeechRecognition) {
    output.textContent =
        "Speech Recognition is not supported. Please use Google Chrome.";
} else {

    const recognition = new SpeechRecognition();

    // English only
    recognition.lang = "en-IN";

    // Show words while speaking
    recognition.interimResults = true;

    // We will automatically restart after every sentence
    recognition.continuous = false;

    recognition.maxAlternatives = 1;

    let isListening = false;
    let shouldKeepListening = false;


    // =========================================
    // START LISTENING
    // =========================================

    function startListening() {

        if (!shouldKeepListening) {
            return;
        }

        try {
            recognition.start();
        } catch (error) {
            // Recognition may already be running.
            console.log("Recognition is already running.");
        }
    }


    // =========================================
    // BUTTON
    // =========================================

    startButton.addEventListener("click", () => {

        if (isListening) {
            shouldKeepListening = false;

            try {
                recognition.stop();
            } catch (error) {
                console.log(error);
            }

            return;
        }

        shouldKeepListening = true;

        output.textContent = "Listening...";

        startListening();
    });


    // =========================================
    // RECOGNITION STARTED
    // =========================================

    recognition.addEventListener("start", () => {

        isListening = true;

        startButton.textContent = "Listening...";

        output.textContent = "Listening...";

        console.log("Listening started");
    });


    // =========================================
    // SPEECH RESULT
    // =========================================

    recognition.addEventListener("result", (event) => {

        let transcript = "";

        for (
            let i = event.resultIndex;
            i < event.results.length;
            i++
        ) {

            transcript += event.results[i][0].transcript;
        }

        transcript = transcript.trim();

        if (transcript) {
            output.textContent = transcript;

            console.log("You:", transcript);
        }
    });


    // =========================================
    // RECOGNITION ENDED
    // =========================================

    recognition.addEventListener("end", () => {

        isListening = false;

        console.log("Recognition ended.");

        if (shouldKeepListening) {

            startButton.textContent = "Listening...";

            output.textContent = "Listening...";

            // Small delay before restarting
            setTimeout(() => {

                if (shouldKeepListening) {
                    startListening();
                }

            }, 300);

        } else {

            startButton.textContent = "Start Listening";
        }
    });


    // =========================================
    // ERROR
    // =========================================

    recognition.addEventListener("error", (event) => {

        console.log("Speech recognition error:", event.error);

        isListening = false;

        // These errors should NOT permanently stop
        // continuous listening.
        if (
            event.error === "no-speech" ||
            event.error === "aborted"
        ) {

            if (shouldKeepListening) {

                setTimeout(() => {
                    startListening();
                }, 500);
            }

            return;
        }


        if (event.error === "not-allowed") {

            shouldKeepListening = false;

            startButton.textContent = "Start Listening";

            output.textContent =
                "Please allow microphone permission.";

            return;
        }


        if (event.error === "network") {

            output.textContent =
                "Network error. Retrying...";

            if (shouldKeepListening) {

                setTimeout(() => {
                    startListening();
                }, 1500);
            }

            return;
        }


        if (shouldKeepListening) {

            setTimeout(() => {
                startListening();
            }, 1000);
        }
    });


    // =========================================
    // ESC = STOP
    // =========================================

    document.addEventListener("keydown", (event) => {

        if (event.key === "Escape") {

            shouldKeepListening = false;

            try {
                recognition.stop();
            } catch (error) {
                console.log(error);
            }

            isListening = false;

            startButton.textContent = "Start Listening";

            output.textContent = "Listening stopped.";
        }
    });
}