#!/usr/bin/env python
import argparse
import sys
from Bio import SeqIO
import numpy as np

# create argument parser
parser = argparse.ArgumentParser(prog="NW", description="Calculate global alignment for 2 Sequences. \n"
                                                        "Input: fasta-file from STDIN.\n"
                                                        "Save results to STDOUT in clustal-format. \n"
                                                        "Save similatrity Value to STDERR. \n",
                                 formatter_class=argparse.RawTextHelpFormatter,
                                 add_help=True)

parser.add_argument("--match", type=int, default=1,
                    help="Score for match. Positive or negative integer. Default: +1")
parser.add_argument("--mismatch", type=int, default=-1,
                    help="Score for mismatch. Positive or negative integer. Default: -1")
parser.add_argument("--gap", type=int, default=-2,
                    help="Score for gap. Positive or negative integer. Default: -2")


# functions
def create_matrix(row_number, column_number):
    matrix = np.zeros(shape=(row_number, column_number), dtype=np.int)
    return matrix


def find_match(character_1, character_2, match_score, mismatch_score):
    if character_1 == character_2:
        return match_score
    else:
        return mismatch_score


def needleman_wunsch(sequence_1, sequence_2, match_score, mismatch_score, gap_score):

    # NW score matrix
    n_seq1 = len(sequence_1)
    m_seq2 = len(sequence_2)

    score_matrix = create_matrix(m_seq2+1, n_seq1+1)

    for i in range(1, m_seq2+1):
        s_next = score_matrix[i - 1, 0] + gap_score
        score_matrix[i, 0] = s_next

    for j in range(1, n_seq1+1):
        s_next = score_matrix[0, j-1] + gap_score
        score_matrix[0, j] = s_next

    for i in range(1, m_seq2+1):
        for j in range(1, n_seq1+1):

            match_find = find_match(sequence_1[j-1], sequence_2[i-1], match_score, mismatch_score)

            s_dia = score_matrix[i-1, j-1] + match_find
            s_right = score_matrix[i-1, j] + gap_score
            s_down = score_matrix[i, j-1] + gap_score

            s_max = max([s_dia, s_right, s_down])
            score_matrix[i, j] = s_max

    # NW traceback
    outSeq1 = ""
    outSeq2 = ""

    i = m_seq2
    j = n_seq1

    while i > 0 and j > 0:
        current_score = score_matrix[i][j]
        dia_score = score_matrix[i-1][j-1]
        up_score = score_matrix[i][j-1]
        left_score = score_matrix[i-1][j]

        if current_score == dia_score + find_match(sequence_1[j-1], sequence_2[i-1], match, mismatch):
            outSeq1 += sequence_1[j-1]
            outSeq2 += sequence_2[i-1]
            i -= 1
            j -= 1
        elif current_score == up_score + gap:
            outSeq1 += sequence_1[j-1]
            outSeq2 += "-"
            j -= 1
        elif current_score == left_score + gap:
            outSeq1 += "-"
            outSeq2 += sequence_2[i-1]
            i -= 1

    while j > 0:
        outSeq1 += sequence_1[j-1]
        outSeq2 += "-"
        j -= 1
    while i > 0:
        outSeq1 += "-"
        outSeq2 += sequence_2[i-1]
        i -= 1

    outSeq1 = outSeq1[::-1]
    outSeq2 = outSeq2[::-1]

    results = [score_matrix, outSeq1, outSeq2]

    return results


def highlight_matches(alignment_1, alignment_2):
    match_highlights = ""
    length = max(len(alignment_2)-1, len(alignment_1)-1)
    i = 0
    while i <= length:
        if alignment_1[i] == alignment_2[i]:
            match_highlights += "*"
            i += 1
        else:
            match_highlights += " "
            i += 1
    return match_highlights


def print_to_clustal(header_list, sequence_list, higlight_string):
    print("CLUSTAL\n\n")
    if len(header_list[0]) == len(header_list[1]):
        spacer = " " * len(header_list[0])

    if len(max(sequence_list[0], sequence_list[1])) <= 60:
        print(f"{header_list[0]}\t{sequence_list[0]}\n"
              f"{header_list[1]}\t{sequence_list[1]}\n"
              f"{spacer}\t{higlight_string}")
    else:
        seqLength = len(sequence_list[0])
        i = 0
        subSeq1 = []
        subSeq2 = []
        subHighlight = []

        while i <= seqLength - 1:
            subSeq1.append(sequence_list[0][i:i + 60])
            subSeq2.append(sequence_list[1][i:i + 60])
            subHighlight.append(higlight_string[i:i + 60])
            i += 60

        i = 0
        while i <= len(subSeq1) - 1:
            print(f"{header_list[0]}\t{subSeq1[i]}\n"
                  f"{header_list[1]}\t{subSeq2[i]}\n"
                  f"{spacer}\t{subHighlight[i]}\n\n")
            i += 1


# test parser
DEBUG = False

if DEBUG:
    args = parser.parse_args(["--match", "1", "--mismatch", "-1", "--gap", "-2"])
else:
    args = parser.parse_args()

    # run NW
    match = args.match
    mismatch = args.mismatch
    gap = args.gap

    if sys.stdin.isatty():  # to avoid getting stuck if no stdin is provided
        parser.print_help()
    else:
        header = []
        sequence = []
        for record in SeqIO.parse(sys.stdin, "fasta"):
            header.append(record.id)
            sequence.append(record.seq)

        sequence1 = sequence[0]
        sequence2 = sequence[1]

        allResults = needleman_wunsch(sequence1, sequence2, match, mismatch, gap)
        scoreMatrix = allResults[0]
        seqAlign = allResults[1:3]

        matchHighlights = highlight_matches(seqAlign[0], seqAlign[1])

        print_to_clustal(header, seqAlign, matchHighlights)
        print(scoreMatrix[-1, -1], file=sys.stderr)





















