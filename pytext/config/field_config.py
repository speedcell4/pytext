#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved
from enum import Enum
from typing import Dict, List, Optional, Union, Tuple

from pytext.common.constants import DatasetFieldName

from .module_config import CNNParams, ModuleConfig, PoolingType
from .pytext_config import ConfigBase


class EmbedInitStrategy(Enum):
    RANDOM = "random"
    ZERO = "zero"


class WordFeatConfig(ConfigBase):
    embed_dim: int = 100
    freeze: bool = False  # only freezes embedding lookup, not MLP layers
    embedding_init_strategy: EmbedInitStrategy = EmbedInitStrategy.RANDOM
    embedding_init_range: Optional[Tuple[float, float]] = None
    export_input_names: List[str] = ["tokens_vals"]
    pretrained_embeddings_path: str = ""
    vocab_file: str = ""
    vocab_size: int = 0
    vocab_from_train_data: bool = True  # build vocab from train data
    vocab_from_all_data: bool = False  # build vocab from train, eval, test data
    lowercase_tokens: bool = True
    min_freq: int = 1
    mlp_layer_dims: Optional[List[int]] = []


class DictFeatConfig(ConfigBase):
    embed_dim: int = 100
    sparse: bool = False
    pooling: PoolingType = PoolingType.MEAN
    export_input_names: List[str] = ["dict_vals", "dict_weights", "dict_lens"]
    vocab_from_train_data: bool = True


class CharFeatConfig(ConfigBase):
    embed_dim: int = 100
    sparse: bool = False
    cnn: CNNParams = CNNParams()
    export_input_names: List[str] = ["char_vals"]
    vocab_from_train_data: bool = True


class PretrainedModelEmbeddingConfig(ConfigBase):
    embed_dim: int = 0
    model_paths: Optional[Dict[str, str]] = None


class FloatVectorConfig(ConfigBase):
    dim: int = 0  # Dimension of the vector in the dataset.


class FeatureConfig(ModuleConfig):  # type: ignore
    word_feat: WordFeatConfig = WordFeatConfig()
    seq_word_feat: Optional[WordFeatConfig] = None
    dict_feat: Optional[DictFeatConfig] = None
    char_feat: Optional[CharFeatConfig] = None
    pretrained_model_embedding: Optional[PretrainedModelEmbeddingConfig] = None


class WordLabelConfig(ConfigBase):
    # Transform sequence labels to BIO format
    use_bio_labels: bool = False
    export_output_names: List[str] = ["word_scores"]
    _name = DatasetFieldName.WORD_LABEL_FIELD


class DocLabelConfig(ConfigBase):
    export_output_names: List[str] = ["doc_scores"]
    label_weights: Dict[str, float] = {}
    _name = DatasetFieldName.DOC_LABEL_FIELD


TargetConfigBase = Union[DocLabelConfig, WordLabelConfig]
