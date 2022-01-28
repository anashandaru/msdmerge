from obspy import read
from obspy.core import Stream
import click

def combine(filelist):
    st = Stream()
    for item in filelist:
        st += read(item)
    return st

def write2file(stream, filename):
    stream.write(filename, format="MSEED")

@click.command()
@click.argument('filename', type=click.Path(exists=True),nargs=-1)
def main(filename):
    stream = combine(filename)
    nameFile = click.prompt('Masukan Nama File keluaran yang diinginkan ', type=str)
    write2file(stream, nameFile+'.mseed')