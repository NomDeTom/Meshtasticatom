"""The path-loss model surface: a name maps to the integer the dispatch has always used.

`conf.MODEL` was a bare integer with no name and no CLI flag, and it sets the largest term in the
link budget. These assert the naming is total and that nothing silently falls back.
"""
import unittest

from lib.config import Config
from lib.phy import (
    PATH_LOSS_MODELS,
    estimate_path_loss,
    path_loss_model_id,
    path_loss_model_name,
)


class PathLossModelNames(unittest.TestCase):
    def test_every_model_the_dispatch_accepts_has_a_name(self):
        """docs/radio_model.md says seven, and the dispatch raises outside [0, 6]."""
        self.assertEqual(sorted(PATH_LOSS_MODELS.values()), list(range(7)))

    def test_names_and_ids_round_trip(self):
        for name, model_id in PATH_LOSS_MODELS.items():
            self.assertEqual(path_loss_model_id(name), model_id)
            self.assertEqual(path_loss_model_name(model_id), name)

    def test_an_unknown_name_raises_rather_than_defaulting(self):
        """A typo must not quietly select model 5 - that is how an arm becomes the default."""
        with self.assertRaises(ValueError):
            path_loss_model_id("3ggp-suburban")
        with self.assertRaises(ValueError):
            path_loss_model_id(7)
        with self.assertRaises(ValueError):
            path_loss_model_name(7)

    def test_the_config_default_is_named(self):
        self.assertEqual(path_loss_model_name(Config().MODEL), "3gpp-suburban")

    def test_naming_a_model_does_not_change_what_it_computes(self):
        """The value is the integer the chain always read, so both forms agree exactly."""
        conf = Config()
        for name, model_id in PATH_LOSS_MODELS.items():
            self.assertEqual(
                estimate_path_loss(conf, 1000.0, 868e6, 10.0, 1.5, model=name),
                estimate_path_loss(conf, 1000.0, 868e6, 10.0, 1.5, model=model_id),
                name,
            )

    def test_the_models_disagree(self):
        """A named set nobody can distinguish would be decoration."""
        conf = Config()
        losses = {
            name: round(estimate_path_loss(conf, 1000.0, 868e6, 10.0, 1.5, model=name), 3)
            for name in PATH_LOSS_MODELS
        }
        self.assertEqual(len(set(losses.values())), len(losses), losses)


if __name__ == "__main__":
    unittest.main()
