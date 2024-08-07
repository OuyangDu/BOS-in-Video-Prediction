PREDNET_LAYER_ORDER = ['conv0', 'pool0', 'conv1', 'pool1', 'conv2', 'pool2', 'conv3', 'pool3']
PREDNET_LAYER_PARA = {
    'conv0': {#'stride': (1, 1),
        'stride': (None, None),
              'kernel_size': (3, 3),
              'padding': ('valide', 'valide'),
              'dilation': (1, 1)},
    'pool0': {'stride': (None, None),
              'kernel_size': (2, 2),
              'padding': ('valide', 'valide'),
              'dilation': (1, 1)},
    'conv1': {'stride': (1, 1),
              'kernel_size': (3, 3),
              'padding': ('valide', 'valide'),
              'dilation': (1, 1)},
    'pool1': {'stride': (None, None),
              'kernel_size': (2, 2),
              'padding': ('valide', 'valide'),
              'dilation': (1, 1)},
    'conv2': {'stride': (1, 1),
              'kernel_size': (3, 3),
              'padding': ('valide', 'valide'),
              'dilation': (1, 1)},
    'pool2': {'stride': (None, None),
              'kernel_size': (2, 2),
              'padding': ('valide', 'valide'),
              'dilation': (1, 1)},
}

PREDNET_MODULE_STACKS = { # the conv and pool layer orders before each E module
    'E0': [],
    'E1': ['conv0', 'pool0'],
    'E2': ['conv0', 'pool0', 'conv1', 'pool1'],
    'E3': ['conv0', 'pool0', 'conv1', 'pool1', 'conv2', 'pool2'],
}
