# -*- coding: utf-8 -*-
# Filename: cider.py
#
# Description: Describes the class to compute the CIDEr
#              (Consensus-Based Image Description Evaluation) Metric
# by Vedantam, Zitnick, and Parikh (http://arxiv.org/abs/1411.5726)
#
# Creation Date: Sun Feb  8 14:16:54 2015
#
# Authors: Ramakrishna Vedantam <vrama91@vt.edu> and
# Tsung-Yi Lin <tl483@cornell.edu>

from .cider_scorer import CiderScorer


class Cider:
    """Main Class to compute the CIDEr metric."""

    def __init__(self, test=None, refs=None, n=4, sigma=6.0):
        # set cider to sum over 1 to 4-grams
        self._n = n
        # set the standard deviation parameter for gaussian penalty
        self._sigma = sigma

    def compute_score(self, gts, res):
        """Main function to compute CIDEr score

        Arguments:
            hypo_for_image (dict): dictionary with key <image> and
                value <tokenized hypothesis / candidate sentence>
            ref_for_image (dict): dictionary with key <image> and value
                <tokenized reference sentence>

        Returns:
            cider (float): computed CIDEr score for the corpus
        """

        cider_scorer = CiderScorer(n=self._n, sigma=self._sigma)
        res = {i: [v] for i, v in enumerate(res)}
        gts = {i: [v] for i, v in enumerate(gts)}
        for id in sorted(gts.keys()):
            hypo = res[id]
            ref = gts[id]

            # Sanity check.
            assert isinstance(hypo, list)
            assert isinstance(ref, list)
            assert len(hypo) == 1
            assert len(ref) > 0

            cider_scorer += (hypo[0], ref)

        (score, scores) = cider_scorer.compute_score()

        return score

    def method(self):
        return "CIDEr"
