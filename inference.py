from funasr import AutoModel
from funasr.utils.postprocess_utils import rich_transcription_postprocess
import time

model_dir = "iic/SenseVoiceSmall"


model = AutoModel(
    model=model_dir,
    trust_remote_code=True,
    remote_code="./model.py",
    vad_model="fsmn-vad",
    vad_kwargs={"max_single_segment_time": 30000},
    device="cuda:0",
)

def process_audio(audio_path):
    """
    示例音频处理函数（需根据实际情况实现）
    这里添加您的语音识别/处理逻辑
    返回: 识别文本/处理结果
    """
    # 示例使用伪代码示意处理流程
    try:
        # point1 = time.time()
        # en
        res = model.generate(
            input=audio_path,
            cache={},
            language="auto",  # "zh", "en", "yue", "ja", "ko", "nospeech"
            use_itn=True,
            batch_size_s=60,
            merge_vad=True,
            merge_length_s=15,
        )
        text = rich_transcription_postprocess(res[0]["text"])
        # point2 = time.time()
        # with open('/home/bsft23/yuwengong2/output.txt', 'w') as f:
        #     print(text, file=f)
            # print("\ntime is ", point2-point1, file=f)
        
        # return "示例处理结果：这是通过音频识别的文本"
        return text
    except Exception as e:
        return str(e)