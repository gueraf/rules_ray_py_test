from absl.testing import absltest

from examples.py_ray_torch.torch_lib import sum_one_to_n


class TorchLibTest(absltest.TestCase):
    def test_sum_one_to_10(self):
        self.assertEqual(sum_one_to_n(10), 55)


if __name__ == "__main__":
    absltest.main()
