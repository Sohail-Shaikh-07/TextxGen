# textxgen/config.py
import random
from typing import List


class Config:
    """
    Configuration class for TextxGen package.
    Stores API key, endpoints, and other configurations.
    """

    # Base URL for OpenRouter API
    BASE_URL = "https://openrouter.ai/api/v1"

    # OpenRouter API URL
    OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

    # Proxy URL for the Vercel deployment
    PROXY_URL = "https://vercel-proxy-alpha-coral.vercel.app"

    # Package version
    VERSION = "1.0.4"

    # Supported models (actual model IDs)
    SUPPORTED_MODELS = {
            "afm_4.5b": "arcee-ai/afm-4.5b",
            "command_r7b_2024": "cohere/command-r7b-12-2024",
            "cydonia_24b": "thedrummer/cydonia-24b-v4.1",
            "deepseek_chat_v3_1": "deepseek/deepseek-chat-v3.1",
            "deepseek_r1_llama_70b": "deepseek/deepseek-r1-distill-llama-70b",
            "devstral_small_2505": "mistralai/devstral-small-2505",
            "gemini_2.5_flash_lite": "google/gemini-2.5-flash-lite",
            "gemini_2.0_flash": "google/gemini-2.0-flash-001",
            "gemma_2_9b": "google/gemma-2-9b-it",
            "gemma_3n_e4b": "google/gemma-3n-e4b-it",
            "granite_4_micro": "ibm-granite/granite-4.0-h-micro",
            "gpt_4.1_nano": "openai/gpt-4.1-nano",
            "gpt_4o_mini": "openai/gpt-4o-mini",
            "gpt_5_nano": "openai/gpt-5-nano",
            "gpt_oss_120b": "openai/gpt-oss-120b",
            "grok4.1_fast": "x-ai/grok-4.1-fast",
            "hermes_l3_70b": "nousresearch/hermes-3-llama-3.1-70b",
            "hermes_l3_8b": "nousresearch/hermes-2-pro-llama-3-8b",
            "internvl3_78b": "opengvlab/internvl3-78b",
            "kat_coder_pro": "kwaipilot/kat-coder-pro:free",
            "kimi_48b": "moonshotai/kimi-linear-48b-a3b-instruct",
            "lfm2_8b": "liquid/lfm2-8b-a1b",
            "lfm_2.2_6b": "liquid/lfm-2.2-6b",
            "llama_3.1_8b": "meta-llama/llama-3.1-8b-instruct",
            "llama_3.2_11b_vision": "meta-llama/llama-3.2-11b-vision-instruct",
            "llama_3.2_1b": "meta-llama/llama-3.2-1b-instruct",
            "llama_3.2_3b": "meta-llama/llama-3.2-3b-instruct",
            "llama_3_8b": "meta-llama/llama-3-8b-instruct",
            "llama_4_maverick": "meta-llama/llama-4-maverick",
            "llama_guard_3_8b": "meta-llama/llama-guard-3-8b",
            "lfm_2.2_6b": "liquid/lfm-2.2-6b",
            "longcat_flash_chat": "meituan/longcat-flash-chat",
            "lunaris_8b": "sao10k/l3-lunaris-8b",
            "ministral_3b": "mistralai/ministral-3b",
            "mistral_24b_2501": "mistralai/mistral-small-24b-instruct-2501",
            "mistral_7b": "mistralai/mistral-7b-instruct",
            "mistral_nemo": "mistralai/mistral-nemo",
            "mistral_small_24b": "mistralai/mistral-small-3.2-24b-instruct",
            "mytho_l2_13b": "gryphe/mythomax-l2-13b",
            "nemotron_12b_v2_vl": "nvidia/nemotron-nano-12b-v2-vl",
            "nemotron_9b_v2": "nvidia/nemotron-nano-9b-v2",
            "nova_lite": "amazon/nova-lite-v1",
            "nova_micro": "amazon/nova-micro-v1",
            "olmo_3_7b": "allenai/olmo-3-7b-instruct",
            "phi_4": "microsoft/phi-4",
            "phi_4_reasoning": "microsoft/phi-4-reasoning-plus",
            "qwen3_14b": "qwen/qwen3-14b",
            "qwen3_30b": "qwen/qwen3-coder-30b-a3b-instruct",
            "qwen3_32b": "qwen/qwen3-32b",
            "qwen3_coder": "qwen/qwen3-coder:free",
            "qwen_2.5_vl_72b": "qwen/qwen2.5-vl-72b-instruct",
            "qwen_vl_8b": "qwen/qwen3-vl-8b-instruct",
            "unslopnemo_12b": "thedrummer/unslopnemo-12b",
            "voxtral_24b": "mistralai/voxtral-small-24b-2507",
    }

    # Default model
    DEFAULT_MODEL = SUPPORTED_MODELS["grok4.1_fast"]

    @staticmethod
    def get_model_display_names() -> dict:
        """
        Returns a dictionary of model display names (without the `:free` suffix).

        Returns:
            dict: Model display names mapped to their keys.
        """
        return {
            "afm_4.5b": "AFM 4.5B",
            "command_r7b_2024": "Command R7B",
            "cydonia_24b": "Cydonia 24B V4.1",
            "deepseek_chat_v3_1": "Deepseek Chat v3.1",
            "deepseek_r1_llama_70b": "Deepseek R1 Distill Llama 70B",
            "devstral_small_2505": "Devstral Small 2505",
            "gemini_2.5_flash_lite": "Gemini 2.5 Flash Lite",
            "gemini_2.0_flash": "Gemini 2.0 Flash",
            "gemma_2_9b": "Gemma 2 9B IT",
            "gemma_3n_e4b": "Gemma 3N E4B IT",
            "granite_4_micro": "Granite 4.0 H Micro",
            "gpt_4.1_nano": "GPT-4.1 Nano",
            "gpt_4o_mini": "GPT-4o Mini",
            "gpt_5_nano": "GPT-5 Nano",
            "gpt_oss_120b": "GPT-OSS 120B",
            "grok4.1_fast": "Grok 4.1 Fast",
            "hermes_l3_70b": "Hermes 3 Llama-3.1 70B",
            "hermes_l3_8b": "Hermes 2 Pro Llama-3 8B",
            "internvl3_78b": "InternVL-3 78B",
            "kat_coder_pro": "Kat Coder Pro",
            "kimi_48b": "Kimi Linear 48B A3B",
            "lfm2_8b": "LFM2 8B A1B",
            "lfm_2.2_6b": "LFM 2.2 6B",
            "llama_3.1_8b": "Llama-3.1 8B Instruct",
            "llama_3.2_11b_vision": "Llama-3.2 11B Vision Instruct",
            "llama_3.2_1b": "Llama-3.2 1B Instruct",
            "llama_3.2_3b": "Llama-3.2 3B Instruct",
            "llama_3_8b": "Llama-3 8B Instruct",
            "llama_4_maverick": "Llama-4 Maverick",
            "llama_guard_3_8b": "Llama Guard-3 8B",
            "longcat_flash_chat": "Longcat Flash Chat",
            "lunaris_8b": "Lunaris 8B",
            "ministral_3b": "Ministral 3B",
            "mistral_24b_2501": "Mistral Small 24B",
            "mistral_7b": "Mistral 7B Instruct",
            "mistral_nemo": "Mistral NEMO",
            "mistral_small_24b": "Mistral Small 3.2 24B",
            "mytho_l2_13b": "MythoMax L2 13B",
            "nemotron_12b_v2_vl": "Nemotron Nano 12B V2 VL",
            "nemotron_9b_v2": "Nemotron Nano 9B V2",
            "nova_lite": "Nova Lite V1",
            "nova_micro": "Nova Micro V1",
            "olmo_3_7b": "OLMo-3 7B Instruct",
            "phi_4": "Phi-4",
            "phi_4_reasoning": "Phi-4 Reasoning+",
            "qwen3_14b": "Qwen-3 14B",
            "qwen3_30b": "Qwen-3 Coder 30B A3B",
            "qwen3_32b": "Qwen-3 32B",
            "qwen3_coder": "Qwen-3 Coder",
            "qwen_2.5_vl_72b": "Qwen-2.5 VL 72B",
            "qwen_vl_8b": "Qwen-3 VL 8B Instruct",
            "unslopnemo_12b": "UnslopNemo-12B",
            "voxtral_24b": "Voxtral Small 24B",
        }
