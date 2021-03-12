{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "YZnWnwAe3UYQ"
   },
   "source": [
    "THỰC HÀNH THỐNG KÊ MÔ TẢ VỚI DỮ LIỆU ĐỊNH LƯỢNG\n",
    "\n",
    "Sử dụng tập dữ liệu microbiome.csv được cung cấp để hoàn thành các bài tập sau"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Eekok-4F3UYU"
   },
   "source": [
    "Câu 1: Tải tập dữ liệu microbiome.csv vào bộ nhớ (sử dụng pandas)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "id": "FiRWXvV93UYU"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "         Taxon  Patient  Tissue  Stool\n",
      "0   Firmicutes        1     632    305\n",
      "1   Firmicutes        2     136   4182\n",
      "2   Firmicutes        3    1174    703\n",
      "3   Firmicutes        4     408   3946\n",
      "4   Firmicutes        5     831   8605\n",
      "..         ...      ...     ...    ...\n",
      "70       Other       11     203      6\n",
      "71       Other       12     392      6\n",
      "72       Other       13      28     25\n",
      "73       Other       14      12     22\n",
      "74       Other       15     305     32\n",
      "\n",
      "[75 rows x 4 columns]\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "\n",
    "save = pd.read_csv('C:\\\\Users\\\\DELL\\\\Downloads\\\\microbiome.csv')\n",
    "print(save)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "KyNIrI8E3UYV"
   },
   "source": [
    "NHÓM CÁC CÂU LỆNH THỰC HIỆN CÁC PHÉP TÍNH HƯỚNG TÂM\n",
    "\n",
    "Câu 2: Hãy tính trung bình cộng của cột Patient"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "id": "DbG7fE6e3UYW"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8.0"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.mean(save['Patient'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "-RrWTwK83UYW"
   },
   "source": [
    "Câu 3: Hãy tính trung bình cộng (mean) đồng thời cho 3 cột Patient, Tissue và Stool"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "id": "3P9D12je3UYW"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Patient      8.000000\n",
       "Tissue     975.000000\n",
       "Stool      723.786667\n",
       "dtype: float64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.mean(save[['Patient', 'Tissue', 'Stool']])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "bm9lvgmj3UYX"
   },
   "source": [
    "Câu 4: Hãy tính trung vị (median) cho 2 cột Tissue và Stool"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {
    "id": "A7E-OO0E3UYX"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Trung vị của cột Tissue là: 310.0\n",
      "Trung vị của cột Stool: 80.0\n",
      "Trung vị của  216.0\n"
     ]
    }
   ],
   "source": [
    "from numpy import median\n",
    "\n",
    "print('Trung vị của cột Tissue là:',median(save['Tissue']))\n",
    "print('Trung vị của cột Stool:',median(save['Stool']))\n",
    "print('Trung vị của 2 cột là ',median(save[['Tissue','Stool']]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "iOD2dh1w3UYX"
   },
   "source": [
    "Câu 5: Hãy tính số yếu vị (mode) cho 3 cột Patient, Tissue và Stool"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {
    "id": "20GjQj4V3UYX"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "số yếu vị của cột Patient là: 1\n",
      "số yếu vị của cột Tissue là: 678\n",
      "số yếu vị của cột Stool là: 2\n"
     ]
    }
   ],
   "source": [
    "import statistics\n",
    "print('số yếu vị của cột Patient là:',statistics.mode(save['Patient']))\n",
    "print('số yếu vị của cột Tissue là:',statistics.mode(save['Tissue']))\n",
    "print('số yếu vị của cột Stool là:',statistics.mode(save['Stool']))\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "xdIc6QSh3UYX"
   },
   "source": [
    "NHÓM CÂU LỆNH TÍNH PHƯƠNG SAI - ĐỘ LỆCH CHUẨN\n",
    "\n",
    "Câu 6: Hãy tính phương sai (variance) của cột Tissue"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "metadata": {
    "id": "J9M4O_u03UYY"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3306370.027027027"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "statistics.variance(save['Tissue'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "Ts2rFB6R3UYY"
   },
   "source": [
    "Câu 7: Hãy tính phương sai của 3 cột Patient, Tissue và Stool"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {
    "id": "9rq8Ax2r3UYY"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Phương sai của cột Patient là : 18.91891891891892\n",
      "Phương sai của cột Tissue là : 3306370.027027027\n",
      "Phương sai của cột Stool là : 2108250.9538738737\n"
     ]
    }
   ],
   "source": [
    "\n",
    "print('Phương sai của cột Patient là :',statistics.variance(save['Patient']))\n",
    "print('Phương sai của cột Tissue là :',statistics.variance(save['Tissue']))\n",
    "print('Phương sai của cột Stool là :',statistics.variance(save['Stool']))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "wi1eoUIr3UYY"
   },
   "source": [
    "Câu 8: Hãy tính độ lệch chuẩn (standard deviation) của 3 cột Patient, Tissue và Stool"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {
    "id": "6Gc_oO673UYY"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Độ lệch chuẩn của cột Patient là : 4.3495883620084\n",
      "Độ lệch chuẩn của cột Tissue là : 1818.342659409119\n",
      "Độ lệch chuẩn của cột Stool là : 1451.9817333127417\n"
     ]
    }
   ],
   "source": [
    "print('Độ lệch chuẩn của cột Patient là :',statistics.stdev(save['Patient']))\n",
    "print('Độ lệch chuẩn của cột Tissue là :',statistics.stdev(save['Tissue']))\n",
    "print('Độ lệch chuẩn của cột Stool là :',statistics.stdev(save['Stool']))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "3YeHBdmo3UYY"
   },
   "source": [
    "NHÓM CÂU LỆNH TÍNH PHÂN VỊ (PERCENTILE)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "LnGc9zBm3UYZ"
   },
   "source": [
    "Câu 9: Tính Q1 Q2 và Q3 cho cột Tissue\n",
    "\n",
    "Tham khảo:\n",
    "\n",
    "1) https://www.geeksforgeeks.org/python-pandas-dataframe-quantile/\n",
    "\n",
    "2) https://stackoverflow.com/questions/45926230/how-to-calculate-1st-and-3rd-quartiles/45926291"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {
    "id": "cjju7ukc3UYZ"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Q1= 108.0\n",
      "Q2= 310.0\n",
      "Q3= 835.0\n"
     ]
    }
   ],
   "source": [
    "q1 = np.percentile(save['Tissue'],25)\n",
    "q2 = np.percentile(save['Tissue'],50)\n",
    "q3 = np.percentile(save['Tissue'],75)\n",
    "print('Q1=',q1)\n",
    "print('Q2=',q2)\n",
    "print('Q3=',q3)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "xJndwy8e3UYZ"
   },
   "source": [
    "Câu 10: Hãy tính z-score cho cột Tissue\n",
    "\n",
    "Gợi ý: sử dụng hàm zscore của thư viện scipy\n",
    "\n",
    "Tham khảo: https://stackoverflow.com/questions/24761998/pandas-compute-z-score-for-all-columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "metadata": {
    "id": "7dU5KxRz3UYZ"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([-0.18990359, -0.46451635,  0.1101773 , -0.31392225, -0.07972629,\n",
       "       -0.15613064, -0.14228928, -0.44403112, -0.41358011, -0.45012133,\n",
       "       -0.33385382,  1.81598764, -0.48057234, -0.48666254, -0.38423641,\n",
       "        0.36707311,  0.82716022, -0.07529705,  1.90401875,  6.12840462,\n",
       "        0.73912911,  1.15049461, -0.32111977,  0.92792539,  0.12180405,\n",
       "        3.25659734, -0.27239815,  1.09346817,  0.3133686 ,  0.18381338,\n",
       "       -0.22478384,  0.34049768, -0.52597203, -0.39641681, -0.22533749,\n",
       "        0.07031416, -0.16443547, -0.39586316, -0.30506378, -0.23641059,\n",
       "       -0.42852879, -0.5165599 , -0.47946503, -0.51157701, -0.36818042,\n",
       "       -0.4761431 , -0.50271853, -0.5398134 , -0.49275274, -0.46064077,\n",
       "       -0.16443547,  2.13378547, -0.49884295, -0.44624574, -0.48112599,\n",
       "       -0.4993966 , -0.52320376, -0.51157701,  0.82937484, -0.48334061,\n",
       "       -0.47669676, -0.43185072, -0.5165599 , -0.36485849, -0.42797514,\n",
       "       -0.47558945, -0.24803734, -0.34215865, -0.48112599, -0.50271853,\n",
       "       -0.42742148, -0.32278073, -0.52431107, -0.53316954, -0.37094869])"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from scipy.stats import zscore\n",
    "zscore(save['Tissue'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "0OlWfP1a3UYZ"
   },
   "source": [
    "NHÓM CÂU LỆNH TỔNG HỢP\n",
    "\n",
    "Câu 11: (bổ sung) Hãy tính giá trị lớn nhất và nhỏ nhất của 3 cột Patient, Tissue và Stool"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {
    "id": "QA8zJjwh3UYZ"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Giá trị lớn nhất và nhỏ nhất của cột Patient lần lượt là: 15 và 1\n",
      "Giá trị lớn nhất và nhỏ nhất của cột Tissue lần lượt là: 12044 và 0\n",
      "Giá trị lớn nhất và nhỏ nhất của cột Stool lần lượt là: 8605 và 0\n"
     ]
    }
   ],
   "source": [
    "print('Giá trị lớn nhất và nhỏ nhất của cột Patient lần lượt là:',max(save['Patient']),'và',min(save['Patient']))\n",
    "print('Giá trị lớn nhất và nhỏ nhất của cột Tissue lần lượt là:',max(save['Tissue']),'và',min(save['Tissue']))\n",
    "print('Giá trị lớn nhất và nhỏ nhất của cột Stool lần lượt là:',max(save['Stool']),'và',min(save['Stool']))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "SpcuMP0Q3UYZ"
   },
   "source": [
    "Câu 12: Hãy thực thi hàm describe đối với data frame chứa dữ liệu của microbiome.csv\n",
    "\n",
    "Tham khảo: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {
    "id": "RTOOotFp3UYa"
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Patient</th>\n",
       "      <th>Tissue</th>\n",
       "      <th>Stool</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>75.000000</td>\n",
       "      <td>75.000000</td>\n",
       "      <td>75.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>8.000000</td>\n",
       "      <td>975.000000</td>\n",
       "      <td>723.786667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>4.349588</td>\n",
       "      <td>1818.342659</td>\n",
       "      <td>1451.981733</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>4.000000</td>\n",
       "      <td>108.000000</td>\n",
       "      <td>16.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>8.000000</td>\n",
       "      <td>310.000000</td>\n",
       "      <td>80.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>12.000000</td>\n",
       "      <td>835.000000</td>\n",
       "      <td>656.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>15.000000</td>\n",
       "      <td>12044.000000</td>\n",
       "      <td>8605.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Patient        Tissue        Stool\n",
       "count  75.000000     75.000000    75.000000\n",
       "mean    8.000000    975.000000   723.786667\n",
       "std     4.349588   1818.342659  1451.981733\n",
       "min     1.000000      0.000000     0.000000\n",
       "25%     4.000000    108.000000    16.000000\n",
       "50%     8.000000    310.000000    80.000000\n",
       "75%    12.000000    835.000000   656.000000\n",
       "max    15.000000  12044.000000  8605.000000"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pd.DataFrame.describe(save)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "KYUmeFmw3UYa"
   },
   "source": [
    "NHÓM CÂU LỆNH ĐỒ HỌA\n",
    "\n",
    "Câu 13: Hãy vẽ biểu đồ box plot cho cột Tissue"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "id": "TSAVziLW3UYa"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 52,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "pd.DataFrame.boxplot(save['Tissue'])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "MwJB69A03UYa"
   },
   "source": [
    "Câu 14: Hãy vẽ biểu đồ box plot cho cả 2 cột Tissue và Stool chung 1 hình (gồm có 2 box plot)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "metadata": {
    "id": "_MHvuLc53UYa"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 77,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "pd.DataFrame.boxplot(save[['Tissue','Stool']])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "QrTRcJrz3UYa"
   },
   "source": [
    "Câu 15: Hãy vẽ lại câu 14 với các box plot nằm ngang"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {
    "id": "PZKPMFaC3UYa"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 78,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "pd.DataFrame.boxplot(save[['Tissue','Stool']],vert = 0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "2LPFwa9Q3UYb"
   },
   "source": [
    "Câu 16: Hãy sử dụng thư viện seaborn để vẽ biểu đồ box plot cho Tissue và Stool"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {
    "id": "Q_eidepH3UYb"
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:>"
      ]
     },
     "execution_count": 91,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import seaborn as sns\n",
    "sns.boxplot(data=(save[['Tissue','Stool']]))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "name": "thuc-hanh-03.ipynb",
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 1
}
