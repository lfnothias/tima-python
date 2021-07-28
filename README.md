## tl;dr:

```
# repo preparation

To run in docker:

```shell
docker build -t tima-python . # optional
docker run -it --rm -v $PWD:/app tima-python
```

To run locally:

```shell
conda env create -f environment.yml &&
conda activate tima-python
```

# get a working structure-organism pairs library

```shell
./src/get_lotus.sh && python src/prepare_lotus.py &&
# python prepare_dnp.py && # only if you have access to it
python src/prepare_library.py &&
python src/prepare_adducts.py &&

```

# get spectral matches

# (did not copy it there, see how we manage this)

./src/get_example_isdb.sh && # get an example result from new isdb without python

# prepare all files for weighting

# NOT READY YET

./src/get_gnverifier.sh && python src/prepare_gnps.py && # optional python src/prepare_isdb.py &&

# python prepare_features_components.py &&

# python prepare_features_classification.py &&

python src/prepare_edges.py && python src/prepare_taxa.py

# And finally the graal!

# NOT READY YET

# python process_annotations.py

# NOTE: you can use --help or -h argument for all .py steps to get more info

```