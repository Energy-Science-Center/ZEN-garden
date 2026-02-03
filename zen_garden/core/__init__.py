from zen_garden.core import preprocess, postprocess, model
from zen_garden.core.utils import get_inheritors
from zen_garden.core.model.element import Element
from zen_garden.core.optimization_setup import OptimizationSetup
from zen_garden.core.runner import run
from zen_garden.core.postprocess.results import Results
from zen_garden.core.utils import download_example_dataset
from zen_garden.core.postprocess.comparisons import compare_model_values, compare_configs, compare_dicts

__all__ = ["run", "Results", "download_example_dataset", "compare_model_values", "compare_configs", "compare_dicts"]


# set the element classes of the EnergySystem class
inheritors = get_inheritors(Element)
OptimizationSetup.dict_element_classes.update({klass.__name__: klass for klass in inheritors})
