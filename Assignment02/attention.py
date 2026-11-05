import numpy as np

H = 12
d_attn = 64
d_mid = 64
d_out = 768


def attention(X,W):
    Q = X @ W[0]+W[3]
    d_attn = Q.shape[1]
    K = X @ W[1]+W[4]
    V = X @ W[2]+W[5]
    S = (Q @ K.T) / np.sqrt(d_attn)
    S_shifted = S - np.max(S, axis=0, keepdims=True)
    exp_S = np.exp(S_shifted)
    attention_weights = exp_S / np.sum(exp_S, axis=0, keepdims=True)
    return  attention_weights @ V


def  MHattention(X, W):
    head_outputs = [
        attention(X, one_head_weight) for one_head_weight in W[0]
    ]

    Y = np.concatenate(head_outputs, axis=1)
    return Y @ W[1] + W[2]
        
def test_MHattn():
    X = np.array([
    [1.0, 0.0],
    [0.0, 1.0],])

    Wq = np.eye(2)
    Wk = np.eye(2)
    Wv = np.eye(2)
    bq = np.zeros(2)
    bk = np.zeros(2)
    bv = np.zeros(2)

    W1 = (Wq, Wk, Wv, bq, bk, bv)
    W2 = (np.eye(4), np.zeros(4))
    W = ([W1, W1], W2)

    result = MHattention(X, W)
    assert result.shape == (2, 4)
    assert np.isfinite(result).all()

def test_attn():
    X = np.array([
    [1.0, 0.0],
    [0.0, 1.0],])

    Wq = np.eye(2)
    Wk = np.eye(2)
    Wv = np.eye(2)
    bq = np.zeros(2)
    bk = np.zeros(2)
    bv = np.zeros(2)

    W = (Wq, Wk, Wv, bq, bk, bv)
    result = attention(X, W)
    assert result.shape == (2, 2)
    assert np.isfinite(result).all()

    p = 1 / (1 + np.exp(-1 / np.sqrt(2)))
    expected = np.array([   
        [p, 1 - p],
        [1 - p, p],
    ])
    np.testing.assert_allclose(result, expected, rtol=1e-6)

    print(result)
    print(result.shape)

if __name__ == "__main__":
    test_attn()
    test_MHattn()