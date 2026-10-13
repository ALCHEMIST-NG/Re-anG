Seeds/runs: 1 (/tmp/claude-0/-home-user-Re-anG/3fa7bfe9-7226-5b7f-a930-0e984d1f84ac/scratchpad/pilot/results_seed0.json)

### adult (seed 0; n_train=4000, n_test=500, features=14, classes=2)

| Learner | clean acc (best k) | cert@1 | cert@2 | cert@5 | cert@10 | cert@15 |
|---|---|---|---|---|---|---|
| TabPFNv1 | 0.830 | 0.812 | 0.800 | 0.768 | 0.732 | 0.700 |
| RF | 0.836 | 0.820 | 0.814 | 0.782 | 0.756 | 0.724 |
| HGB | 0.844 | 0.812 | 0.782 | 0.742 | 0.682 | 0.668 |
| HGB-small | 0.852 | 0.812 | 0.794 | 0.770 | 0.722 | 0.674 |
| LogReg | 0.814 | 0.800 | 0.792 | 0.776 | 0.744 | 0.714 |
| kNN (best K) | 0.818 | 0.802 | 0.798 | 0.784 | 0.754 | 0.716 |

Per-partition mean accuracy (single base learner on one partition):

| Learner | m=400 | m=200 | m=100 | m=50 | retention 50/400 |
|---|---|---|---|---|---|
| TabPFNv1 | 0.823 | 0.815 | 0.796 | 0.780 | 0.947 |
| RF | 0.828 | 0.819 | 0.807 | 0.789 | 0.954 |
| HGB | 0.815 | 0.788 | 0.772 | 0.750 | 0.920 |
| HGB-small | 0.821 | 0.803 | 0.784 | 0.759 | 0.924 |
| LogReg | 0.815 | 0.802 | 0.784 | 0.767 | 0.941 |

### kr_vs_kp (seed 0; n_train=2696, n_test=500, features=36, classes=2)

| Learner | clean acc (best k) | cert@1 | cert@2 | cert@5 | cert@10 | cert@15 |
|---|---|---|---|---|---|---|
| TabPFNv1 | 0.982 | 0.972 | 0.956 | 0.918 | 0.786 | 0.656 |
| RF | 0.984 | 0.970 | 0.962 | 0.918 | 0.808 | 0.652 |
| HGB | 0.988 | 0.970 | 0.950 | 0.874 | 0.626 | 0.192 |
| HGB-small | 0.988 | 0.978 | 0.968 | 0.932 | 0.890 | 0.818 |
| LogReg | 0.976 | 0.956 | 0.936 | 0.902 | 0.792 | 0.626 |
| kNN (best K) | 0.916 | 0.898 | 0.876 | 0.802 | 0.738 | 0.696 |

Per-partition mean accuracy (single base learner on one partition):

| Learner | m=400 | m=200 | m=100 | m=50 | retention 50/400 |
|---|---|---|---|---|---|
| TabPFNv1 | 0.975 | 0.952 | 0.920 | 0.818 | 0.839 |
| RF | 0.969 | 0.955 | 0.911 | 0.819 | 0.845 |
| HGB | 0.974 | 0.951 | 0.861 | 0.608 | 0.625 |
| HGB-small | 0.977 | 0.960 | 0.937 | 0.893 | 0.914 |
| LogReg | 0.963 | 0.946 | 0.906 | 0.813 | 0.845 |

### magic (seed 0; n_train=4000, n_test=500, features=10, classes=2)

| Learner | clean acc (best k) | cert@1 | cert@2 | cert@5 | cert@10 | cert@15 |
|---|---|---|---|---|---|---|
| TabPFNv1 | 0.858 | 0.836 | 0.822 | 0.786 | 0.752 | 0.730 |
| RF | 0.840 | 0.812 | 0.798 | 0.764 | 0.732 | 0.698 |
| HGB | 0.846 | 0.832 | 0.810 | 0.754 | 0.682 | 0.626 |
| HGB-small | 0.848 | 0.828 | 0.814 | 0.780 | 0.740 | 0.694 |
| LogReg | 0.792 | 0.786 | 0.782 | 0.770 | 0.748 | 0.720 |
| kNN (best K) | 0.812 | 0.792 | 0.774 | 0.756 | 0.734 | 0.720 |

Per-partition mean accuracy (single base learner on one partition):

| Learner | m=400 | m=200 | m=100 | m=50 | retention 50/400 |
|---|---|---|---|---|---|
| TabPFNv1 | 0.845 | 0.826 | 0.809 | 0.769 | 0.910 |
| RF | 0.824 | 0.808 | 0.788 | 0.759 | 0.921 |
| HGB | 0.828 | 0.805 | 0.778 | 0.726 | 0.877 |
| HGB-small | 0.825 | 0.805 | 0.776 | 0.749 | 0.907 |
| LogReg | 0.787 | 0.784 | 0.772 | 0.755 | 0.959 |

### mushroom (seed 0; n_train=4000, n_test=500, features=22, classes=2)

| Learner | clean acc (best k) | cert@1 | cert@2 | cert@5 | cert@10 | cert@15 |
|---|---|---|---|---|---|---|
| TabPFNv1 | 0.996 | 0.994 | 0.992 | 0.964 | 0.940 | 0.926 |
| RF | 0.996 | 0.996 | 0.996 | 0.980 | 0.966 | 0.926 |
| HGB | 0.994 | 0.994 | 0.984 | 0.978 | 0.928 | 0.890 |
| HGB-small | 0.998 | 0.992 | 0.988 | 0.982 | 0.966 | 0.952 |
| LogReg | 0.946 | 0.944 | 0.942 | 0.934 | 0.918 | 0.894 |
| kNN (best K) | 0.990 | 0.990 | 0.990 | 0.978 | 0.964 | 0.952 |

Per-partition mean accuracy (single base learner on one partition):

| Learner | m=400 | m=200 | m=100 | m=50 | retention 50/400 |
|---|---|---|---|---|---|
| TabPFNv1 | 0.990 | 0.980 | 0.961 | 0.926 | 0.936 |
| RF | 0.993 | 0.986 | 0.972 | 0.941 | 0.948 |
| HGB | 0.991 | 0.982 | 0.959 | 0.829 | 0.836 |
| HGB-small | 0.991 | 0.984 | 0.970 | 0.938 | 0.947 |
| LogReg | 0.946 | 0.940 | 0.926 | 0.898 | 0.950 |

### phoneme (seed 0; n_train=4000, n_test=500, features=5, classes=2)

| Learner | clean acc (best k) | cert@1 | cert@2 | cert@5 | cert@10 | cert@15 |
|---|---|---|---|---|---|---|
| TabPFNv1 | 0.870 | 0.836 | 0.810 | 0.750 | 0.660 | 0.624 |
| RF | 0.882 | 0.854 | 0.834 | 0.778 | 0.724 | 0.662 |
| HGB | 0.870 | 0.848 | 0.834 | 0.774 | 0.748 | 0.672 |
| HGB-small | 0.872 | 0.860 | 0.836 | 0.780 | 0.706 | 0.632 |
| LogReg | 0.780 | 0.770 | 0.768 | 0.746 | 0.702 | 0.670 |
| kNN (best K) | 0.862 | 0.836 | 0.820 | 0.802 | 0.780 | 0.756 |

Per-partition mean accuracy (single base learner on one partition):

| Learner | m=400 | m=200 | m=100 | m=50 | retention 50/400 |
|---|---|---|---|---|---|
| TabPFNv1 | 0.843 | 0.824 | 0.796 | 0.762 | 0.904 |
| RF | 0.849 | 0.828 | 0.804 | 0.776 | 0.915 |
| HGB | 0.841 | 0.835 | 0.793 | 0.755 | 0.898 |
| HGB-small | 0.839 | 0.825 | 0.799 | 0.760 | 0.906 |
| LogReg | 0.774 | 0.773 | 0.765 | 0.753 | 0.973 |

### ring (seed 0; n_train=4000, n_test=500, features=20, classes=2)

| Learner | clean acc (best k) | cert@1 | cert@2 | cert@5 | cert@10 | cert@15 |
|---|---|---|---|---|---|---|
| TabPFNv1 | 0.972 | 0.972 | 0.972 | 0.964 | 0.954 | 0.940 |
| RF | 0.952 | 0.946 | 0.942 | 0.924 | 0.870 | 0.808 |
| HGB | 0.952 | 0.936 | 0.924 | 0.850 | 0.690 | 0.484 |
| HGB-small | 0.952 | 0.940 | 0.922 | 0.874 | 0.776 | 0.708 |
| LogReg | 0.764 | 0.744 | 0.732 | 0.698 | 0.632 | 0.552 |
| kNN (best K) | 0.566 | 0.550 | 0.540 | 0.514 | 0.506 | 0.504 |

Per-partition mean accuracy (single base learner on one partition):

| Learner | m=400 | m=200 | m=100 | m=50 | retention 50/400 |
|---|---|---|---|---|---|
| TabPFNv1 | 0.966 | 0.965 | 0.958 | 0.925 | 0.958 |
| RF | 0.920 | 0.913 | 0.892 | 0.827 | 0.898 |
| HGB | 0.931 | 0.894 | 0.799 | 0.641 | 0.688 |
| HGB-small | 0.925 | 0.884 | 0.832 | 0.752 | 0.813 |
| LogReg | 0.745 | 0.726 | 0.707 | 0.676 | 0.907 |

### satimage (seed 0; n_train=4000, n_test=500, features=36, classes=6)

| Learner | clean acc (best k) | cert@1 | cert@2 | cert@5 | cert@10 | cert@15 |
|---|---|---|---|---|---|---|
| TabPFNv1 | 0.884 | 0.860 | 0.844 | 0.812 | 0.772 | 0.726 |
| RF | 0.884 | 0.872 | 0.856 | 0.824 | 0.796 | 0.760 |
| HGB | 0.892 | 0.862 | 0.860 | 0.816 | 0.722 | 0.608 |
| HGB-small | 0.886 | 0.870 | 0.854 | 0.830 | 0.784 | 0.712 |
| LogReg | 0.840 | 0.828 | 0.816 | 0.798 | 0.764 | 0.730 |
| kNN (best K) | 0.876 | 0.868 | 0.858 | 0.838 | 0.814 | 0.788 |

Per-partition mean accuracy (single base learner on one partition):

| Learner | m=400 | m=200 | m=100 | m=50 | retention 50/400 |
|---|---|---|---|---|---|
| TabPFNv1 | 0.868 | 0.848 | 0.819 | 0.788 | 0.908 |
| RF | 0.871 | 0.852 | 0.821 | 0.789 | 0.906 |
| HGB | 0.860 | 0.833 | 0.788 | 0.647 | 0.752 |
| HGB-small | 0.859 | 0.830 | 0.787 | 0.734 | 0.854 |
| LogReg | 0.830 | 0.820 | 0.806 | 0.788 | 0.949 |

### spambase (seed 0; n_train=4000, n_test=500, features=57, classes=2)

| Learner | clean acc (best k) | cert@1 | cert@2 | cert@5 | cert@10 | cert@15 |
|---|---|---|---|---|---|---|
| TabPFNv1 | 0.956 | 0.948 | 0.942 | 0.936 | 0.904 | 0.888 |
| RF | 0.934 | 0.926 | 0.920 | 0.892 | 0.870 | 0.840 |
| HGB | 0.952 | 0.936 | 0.924 | 0.876 | 0.810 | 0.738 |
| HGB-small | 0.948 | 0.934 | 0.930 | 0.902 | 0.858 | 0.806 |
| LogReg | 0.940 | 0.936 | 0.928 | 0.888 | 0.852 | 0.822 |
| kNN (best K) | 0.900 | 0.882 | 0.872 | 0.854 | 0.822 | 0.798 |

Per-partition mean accuracy (single base learner on one partition):

| Learner | m=400 | m=200 | m=100 | m=50 | retention 50/400 |
|---|---|---|---|---|---|
| TabPFNv1 | 0.943 | 0.934 | 0.920 | 0.900 | 0.955 |
| RF | 0.931 | 0.916 | 0.898 | 0.868 | 0.932 |
| HGB | 0.928 | 0.911 | 0.867 | 0.783 | 0.844 |
| HGB-small | 0.924 | 0.908 | 0.875 | 0.837 | 0.906 |
| LogReg | 0.897 | 0.887 | 0.868 | 0.838 | 0.934 |

### twonorm (seed 0; n_train=4000, n_test=500, features=20, classes=2)

| Learner | clean acc (best k) | cert@1 | cert@2 | cert@5 | cert@10 | cert@15 |
|---|---|---|---|---|---|---|
| TabPFNv1 | 0.978 | 0.978 | 0.976 | 0.974 | 0.964 | 0.956 |
| RF | 0.980 | 0.980 | 0.974 | 0.962 | 0.948 | 0.920 |
| HGB | 0.978 | 0.964 | 0.958 | 0.934 | 0.900 | 0.852 |
| HGB-small | 0.970 | 0.964 | 0.956 | 0.942 | 0.894 | 0.830 |
| LogReg | 0.978 | 0.976 | 0.976 | 0.972 | 0.966 | 0.956 |
| kNN (best K) | 0.978 | 0.976 | 0.976 | 0.972 | 0.970 | 0.966 |

Per-partition mean accuracy (single base learner on one partition):

| Learner | m=400 | m=200 | m=100 | m=50 | retention 50/400 |
|---|---|---|---|---|---|
| TabPFNv1 | 0.972 | 0.969 | 0.967 | 0.962 | 0.990 |
| RF | 0.962 | 0.956 | 0.943 | 0.915 | 0.951 |
| HGB | 0.948 | 0.931 | 0.906 | 0.824 | 0.869 |
| HGB-small | 0.941 | 0.915 | 0.877 | 0.818 | 0.869 |
| LogReg | 0.970 | 0.968 | 0.965 | 0.960 | 0.990 |

### waveform_40 (seed 0; n_train=4000, n_test=500, features=40, classes=3)

| Learner | clean acc (best k) | cert@1 | cert@2 | cert@5 | cert@10 | cert@15 |
|---|---|---|---|---|---|---|
| TabPFNv1 | 0.848 | 0.830 | 0.802 | 0.758 | 0.678 | 0.582 |
| RF | 0.828 | 0.800 | 0.794 | 0.770 | 0.724 | 0.678 |
| HGB | 0.836 | 0.798 | 0.780 | 0.718 | 0.636 | 0.560 |
| HGB-small | 0.832 | 0.806 | 0.794 | 0.764 | 0.696 | 0.606 |
| LogReg | 0.856 | 0.836 | 0.818 | 0.776 | 0.726 | 0.648 |
| kNN (best K) | 0.820 | 0.804 | 0.788 | 0.760 | 0.702 | 0.652 |

Per-partition mean accuracy (single base learner on one partition):

| Learner | m=400 | m=200 | m=100 | m=50 | retention 50/400 |
|---|---|---|---|---|---|
| TabPFNv1 | 0.820 | 0.804 | 0.767 | 0.693 | 0.845 |
| RF | 0.810 | 0.795 | 0.782 | 0.749 | 0.924 |
| HGB | 0.801 | 0.785 | 0.749 | 0.682 | 0.852 |
| HGB-small | 0.799 | 0.782 | 0.756 | 0.715 | 0.894 |
| LogReg | 0.811 | 0.788 | 0.762 | 0.733 | 0.905 |

## Accuracy vs. vote stability (r = 5)

Within-group slope b = 0.99, within-group correlation = 0.86, groups = 39

| Learner | mean residual cert@5 (pp) | n cells |
|---|---|---|
| LogReg | +0.41 | 39 |
| HGB-small | +0.19 | 39 |
| RF | +0.10 | 39 |
| TabPFNv1 | -0.15 | 39 |
| HGB | -0.54 | 39 |

## Aggregate over 10 dataset-runs (best-over-k per learner)

| radius r | best TFM best overall | best TFM beats all non-TFM DPA learners | kNN >= every DPA learner | median margin (best TFM − best non-TFM incl. kNN) |
|---|---|---|---|---|
| 1 | 3/10 | 3/10 | 0/10 | -0.004 |
| 2 | 3/10 | 3/10 | 1/10 | -0.008 |
| 5 | 4/10 | 4/10 | 3/10 | -0.015 |
| 10 | 3/10 | 3/10 | 3/10 | -0.025 |
| 15 | 3/10 | 3/10 | 4/10 | -0.025 |
