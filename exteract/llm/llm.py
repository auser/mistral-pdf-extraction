from langchain.llms import CTransformers
import box, os
import yaml
from exteract.paths import BASE_DIR


# Import config vars
with open(BASE_DIR / "config.yml", "r", encoding="utf8") as ymlfile:
    cfg = box.Box(yaml.safe_load(ymlfile))


def setup_llm():
    llm = CTransformers(
        model=os.path.realpath(BASE_DIR / cfg.MODEL_BIN_PATH),
        model_type=cfg.MODEL_TYPE,
        max_new_tokens=cfg.MAX_NEW_TOKENS,
        temperature=cfg.TEMPERATURE,
    )

    return llm
