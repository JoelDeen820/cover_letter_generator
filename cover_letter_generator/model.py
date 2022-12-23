import torch
from torch import nn

class ResumeNLP(nn.Module):

    def __init__(self, vocab_size : int, n_hidden=256, n_layers=4, dropout_prob=0.3, lr=0.003):
        super().__init__()

        self.drop_prob = dropout_prob
        self.n_layers = n_layers
        self.n_hidden = n_hidden
        self.lr = lr

        self.intermediate_layer_size = 200
        self.emb_layer = nn.Embedding(vocab_size, self.intermediate_layer_size)

        self.lstm = nn.LSTM(self.intermediate_layer_size, self.n_hidden, self.n_layers,
                                dropout=self.drop_prob, batch_first=True)

        self.dropout = nn.Dropout(dropout_prob)

        self.fc = nn.Linear(self.n_hidden, vocab_size)

    def forward(self, x, hidden):
        embedded = self.emb_layer(x)
        lstm_output, hidden = self.lstm(embedded, hidden)
        out = self.dropout(lstm_output)
        out = out.reshape(-1, self.n_hidden)
        out = self.fc(out)
        return out, hidden

    def init_hidden(self, batch_size):

        weight = next(self.parameters()).data
        if torch.cuda.is_available():
            hidden = (weight.new(self.n_layers, batch_size, self.n_hidden).zero_().cuda(),
                      weight.new(self.n_layers, batch_size, self.n_hidden).zero_().cuda())
        else :
            hidden = (weight.new(self.n_layers, batch_size, self.n_hidden).zero_(),
                      weight.new(self.n_layers, batch_size, self.n_hidden).zero_())
        return hidden
