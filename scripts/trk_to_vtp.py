"""
Convert a .trk tractography file to .vtp (VTK PolyData XML)
for visualization in 3D Slicer.

Requirements:
    pip install dipy nibabel
"""

from dipy.io.streamline import load_tractogram, save_tractogram
from dipy.io.stateful_tractogram import Space


def trk_to_vtp(in_trk, out_vtp):
    """
    Convert TRK file to VTK PolyData (.vtp) in RAS+ mm space.

    Parameters
    ----------
    in_trk : str
        Path to input .trk file
    out_vtp : str
        Path to output .vtp file
    """
    # Load tractogram using its own reference
    sft = load_tractogram(in_trk, reference="same")

    # Convert to RAS+ millimeter space (expected by 3D Slicer)
    sft.to_space(Space.RASMM)

    # Save as VTK PolyData XML
    save_tractogram(sft, out_vtp, bbox_valid_check=False)

    print(f"Wrote {out_vtp}")


if __name__ == "__main__":
    in_trk = "your_file.trk"
    out_vtp = "your_file.vtp"

    trk_to_vtp(in_trk, out_vtp)
