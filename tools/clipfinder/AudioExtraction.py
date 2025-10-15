import os
import ffmpeg
from tools.clipfinder.VideoInput import VideoInput
import whisperx


class AudioExtraction:
    def transcribe(self, video):
        # Validate the video file
        video_input = VideoInput(video)

        # Convert video to audio (.wav)
        audio_path = os.path.splitext(video_input.path)[0] + ".wav"
        ffmpeg.input(video_input.path).output(
            audio_path, acodec='pcm_s16le', ac=1, ar='16000'
        ).run(overwrite_output=True)

        # Load WhisperX model
        model = whisperx.load_model("base", device="cuda", compute_type="float32")

        # Transcribe the extracted audio
        result = model.transcribe(audio_path)
        return result


if __name__ == "__main__":
    # Detect current folder
    here = os.path.dirname(__file__)
    video_path = os.path.join(here, "example.mp4")  # local video file

    extractor = AudioExtraction()

    try:
        result = extractor.transcribe(video_path)
        print("✅ Transcription complete!\n")
        print(result["text"])  # Print the transcribed text
    except Exception as e:
        print("❌ Error:", e)
