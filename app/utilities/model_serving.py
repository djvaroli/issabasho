from typing import *
import grpc
import json

from tensorflow_serving.apis.model_pb2 import ModelSpec
import numpy as np
from tensorflow_serving.apis import predict_pb2, get_model_metadata_pb2, prediction_service_pb2_grpc
from google.protobuf.json_format import MessageToJson
from tensorflow import make_tensor_proto


def _get_serving_stub_and_channel(
        model_uri: str,
):
    channel = grpc.insecure_channel(model_uri)
    return prediction_service_pb2_grpc.PredictionServiceStub(channel), channel


def _get_model_spec(
        model_name: str,
        signature_name: str = "",
        version_label: Optional[str] = None,
        version: Optional[int] = None
):
    return ModelSpec(name=model_name, signature_name=signature_name)


def _get_model_metadata(
        model_uri: str,
        model_name: str,
        version_label: Optional[str] = None,
        version: Optional[int] = None,
        signature_name: str = "serving_default",
        timeout: float = 1.0
):
    serving_stub, channel = _get_serving_stub_and_channel(model_uri)

    # let the helper function handle fetching the right ModelSpec
    model_spec = _get_model_spec(model_name, signature_name=signature_name)
    request = get_model_metadata_pb2.GetModelMetadataRequest(model_spec=model_spec)
    request.metadata_field.append('signature_def')

    result = serving_stub.GetModelMetadata(request, timeout)
    _metadata = json.loads(MessageToJson(result))
    channel.close()

    return _metadata


def _get_model_prediction(
        inputs: np.ndarray,
        model_uri: str,
        model_name: str,
        input_layer_name: str,
        version_label: Optional[str] = None,
        version: Optional[int] = None,
        timeout: Optional[float] = 1.0
):
    serving_stub, channel = _get_serving_stub_and_channel(model_uri)
    model_spec = _get_model_spec(model_name, "serving_default", version_label, version)

    request = predict_pb2.PredictRequest(model_spec=model_spec)
    request.inputs[input_layer_name].CopyFrom(make_tensor_proto(inputs.astype(np.float32), shape=inputs.shape))
    result = serving_stub.Predict(request, timeout)
    channel.close()
    return result


def get_model_info(
        info_to_fetch: List[str],
        model_uri: str,
        model_name: str,
        version_label: Optional[str] = None,
        version: Optional[int] = None,
        signature_name: Optional[str] = "serving_default",
        *args,
        **kwargs
):
    def _fetch_input_names() -> List[str]:
        inputs_ = signature_def[signature_name]['inputs']
        return list(inputs_.keys())

    def _fetch_output_names() -> List[str]:
        outputs_ = signature_def[signature_name]
        return list(outputs_.keys())

    def _fetch_input_sizes() -> List[int]:
        pass

    metadata = _get_model_metadata(model_uri, model_name, version_label, version, )
    signature_def = metadata['metadata']['signature_def']['signatureDef']

    info_function_map = {
        "input_name":  _fetch_input_names
    }


def get_input_name(
        model_uri: str,
        model_name: str,
        version_label: Optional[str] = None,
        version: Optional[int] = None
):
    metadata = _get_model_metadata(model_uri, model_name, version_label, version)
    signature_def = metadata['metadata']['signature_def']['signatureDef']
    inputs = signature_def['serving_default']['inputs']

    return list(inputs.keys())[0]


def get_output_size(
        model_uri: str,
        model_name: str,
        output_name: str,
        version_label: Optional[str] = None,
        version: Optional[int] = None
) -> int:
    metadata = _get_model_metadata(model_uri, model_name, version_label, version)

    signature_def = metadata['metadata']['signature_def']['signatureDef']
    outputs = signature_def['serving_default']['outputs']
    n = int(outputs[output_name]['tensorShape']['dim'][-1]['size'])

    return n


def get_output_name(
        model_uri: str,
        model_name: str,
        version_label: Optional[str] = None,
        version: Optional[int] = None
):
    metadata = _get_model_metadata(model_uri, model_name, version_label, version)
    signature_def = metadata['metadata']['signature_def']['signatureDef']
    outputs = signature_def['serving_default']['outputs']

    return list(outputs.keys())[0]


def get_model_input_output_names(
        model_uri: str,
        model_name: str,
        version_label: str,
        version: Union[int, None]
):
    """
    The pruned model does not have the correct input and output layer names assigned, so this will be a temporary
    helper function to fetch those so that we do not need to hard code them.
    :param model_uri:
    :param model_name:
    :param version_label:
    :param version:
    :return:
    """
    input_name = get_input_name(model_uri, model_name, version_label, version)
    output_name = get_output_name(model_uri, model_name, version_label, version)

    return input_name, output_name


def get_haiku_scores():
    metadata = _get_model_metadata('localhost:8500', "haiku")