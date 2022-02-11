from pathlib import Path

from tqdm.auto import tqdm
from matplotlib import animation
from matplotlib import pyplot as plt
from matplotlib.patches import Arc, Wedge, Rectangle


def plot_handball_pitch(xmin, xmax, ymin, ymax, figsize, show=False):
    """
        This function plots a handball pitch for given size values of the pitch.
        The size values of the pitch must be in the ration of 2:1 (long side:short side)

        Parameters
        ----------
        xmin : int
            x-coordinate of the left outer line of the field.
        xmax : int
            x-coordinate of the right outer line of the field.
        ymin : int
            y-coordinate of the lower outer line of the field.
        ymax : int
            y-coordinate of the upper outer line of the field.
        show: bool
            True will show the plot after calling the function.

        Returns
        -------
        matplotlib.axes._subplots.AxesSubplot
            An subplot to which all elements of the handball pitch are added.
        """

    fig, ax = plt.subplots(figsize=figsize)

    x_range = xmax - xmin
    y_range = ymax - ymin
    x_half = (xmax + xmin) / 2
    y_half = (ymax + ymin) / 2

    ax.set_xlim([xmin - (x_range * 0.025), xmax + (x_range * 0.025)])
    ax.set_ylim([ymin - (y_range * 0.05), ymax + (y_range * 0.05)])

    ax.set_facecolor("skyblue")
    outline = "white"
    innerline = "white"
    fill = "khaki"
    # center_spot = plt.Circle((x_half, y_half), (y_range * 0.00625), edgecolor=outline)

    # main boundaries
    ax.plot(
        [xmin, xmin],
        [ymin, ymax],
        color=outline,
        scalex=False,
        scaley=False,
        linewidth=2,
    )
    ax.plot(
        [xmax, xmax],
        [ymin, ymax],
        color=outline,
        scalex=False,
        scaley=False,
        linewidth=2,
    )
    ax.plot(
        [xmin, xmax],
        [ymin, ymin],
        color=outline,
        scalex=False,
        scaley=False,
        linewidth=2,
    )
    ax.plot(
        [xmin, xmax],
        [ymax, ymax],
        color=outline,
        scalex=False,
        scaley=False,
        linewidth=2,
    )

    # midline
    ax.plot([x_half, x_half], [ymin, ymax], color=outline, scalex=False, scaley=False)

    # ax.add_patch(center_spot)

    # free-throw lines
    # lower left
    ax.add_patch(
        Arc(
            (xmin, ymin + (y_range * 0.425)),
            width=(y_range * 0.9),
            height=(y_range * 0.9),
            angle=0,
            theta1=290,
            theta2=360,
            linestyle="dashed",
            linewidth=1,
            color=innerline,
        )
    )
    # above left
    ax.add_patch(
        Arc(
            (xmin, ymin + (y_range * 0.575)),
            width=(y_range * 0.9),
            height=(y_range * 0.9),
            angle=0,
            theta1=0,
            theta2=70,
            linestyle="dashed",
            linewidth=1,
            color=innerline,
        )
    )
    # lower right
    ax.add_patch(
        Arc(
            (xmax, ymin + (y_range * 0.425)),
            width=(y_range * 0.9),
            height=(y_range * 0.9),
            angle=0,
            theta1=180,
            theta2=250,
            linestyle="dashed",
            linewidth=1,
            color=innerline,
        )
    )
    # above right
    ax.add_patch(
        Arc(
            (xmax, ymin + (y_range * 0.575)),
            width=(y_range * 0.9),
            height=(y_range * 0.9),
            angle=0,
            theta1=110,
            theta2=180,
            linestyle="dashed",
            linewidth=1,
            color=innerline,
        )
    )

    # goal area lines
    # lower left
    ax.add_patch(
        Wedge(
            (xmin, ymin + (y_range * 0.425)),
            r=(y_range * 0.3),
            theta1=270,
            theta2=360,
            linewidth=1,
            color=fill,
        )
    )
    ax.add_patch(
        Arc(
            (xmin, ymin + (y_range * 0.425)),
            width=(y_range * 0.6),
            height=(y_range * 0.6),
            angle=0,
            theta1=270,
            theta2=360,
            linewidth=2,
            color=outline,
        )
    )
    # upper left
    ax.add_patch(
        Wedge(
            (xmin, ymin + (y_range * 0.575)),
            r=(y_range * 0.3),
            theta1=0,
            theta2=90,
            linewidth=1,
            color=fill,
        )
    )
    ax.add_patch(
        Arc(
            (xmin, ymin + (y_range * 0.575)),
            (y_range * 0.6),
            (y_range * 0.6),
            angle=0,
            theta1=0,
            theta2=90,
            linewidth=2,
            color=outline,
        )
    )
    # lower right
    ax.add_patch(
        Wedge(
            (xmax, ymin + (y_range * 0.425)),
            r=(y_range * 0.3),
            theta1=180,
            theta2=270,
            linewidth=1,
            color=fill,
        )
    )
    ax.add_patch(
        Arc(
            (xmax, ymin + (y_range * 0.425)),
            (y_range * 0.6),
            (y_range * 0.6),
            angle=0,
            theta1=180,
            theta2=270,
            linewidth=2,
            color=outline,
        )
    )
    # upper right
    ax.add_patch(
        Wedge(
            (xmax, ymin + (y_range * 0.575)),
            r=(y_range * 0.3),
            theta1=90,
            theta2=180,
            linewidth=1,
            color=fill,
        )
    )
    ax.add_patch(
        Arc(
            (xmax, ymin + (y_range * 0.575)),
            (y_range * 0.6),
            (y_range * 0.6),
            angle=0,
            theta1=90,
            theta2=180,
            linewidth=2,
            color=outline,
        )
    )
    # mid left
    ax.add_patch(
        Rectangle(
            (xmin, ymin + (y_range * 0.425)),
            width=(y_range * 0.3),
            height=(y_range * 0.15),
            color=fill,
        )
    )
    # mid right
    ax.add_patch(
        Rectangle(
            (xmax - (y_range * 0.3), ymin + (y_range * 0.425)),
            width=(y_range * 0.3),
            height=(y_range * 0.15),
            color=fill,
        )
    )

    # vertical goal area lines
    ax.plot(
        [xmin + (x_range * 0.15), xmin + (x_range * 0.15)],
        [ymin + (y_range * 0.425), ymin + (y_range * 0.575)],
        color=outline,
        linewidth=2,
        scalex=False,
        scaley=False,
    )
    ax.plot(
        [xmax - (x_range * 0.15), xmax - (x_range * 0.15)],
        [ymin + (y_range * 0.425), ymin + (y_range * 0.575)],
        color=outline,
        linewidth=2,
        scalex=False,
        scaley=False,
    )

    ax.plot(
        [xmin + (x_range * 0.225), xmin + (x_range * 0.225)],
        [ymin + (y_range * 0.425), ymin + (y_range * 0.575)],
        color=innerline,
        linewidth=1,
        linestyle="dashed",
        scalex=False,
        scaley=False,
    )
    ax.plot(
        [xmax - (x_range * 0.225), xmax - (x_range * 0.225)],
        [ymin + (y_range * 0.425), ymin + (y_range * 0.575)],
        color=innerline,
        linewidth=1,
        linestyle="dashed",
        scalex=False,
        scaley=False,
    )

    # 4 m lines
    ax.plot(
        [xmin + (x_range * 0.1), xmin + (x_range * 0.1)],
        [ymin + (y_range * 0.49625), ymin + (y_range * 0.50375)],
        color=outline,
        linewidth=2,
        scalex=False,
        scaley=False,
    )
    ax.plot(
        [xmax - (x_range * 0.1), xmax - (x_range * 0.1)],
        [ymin + (y_range * 0.49625), ymin + (y_range * 0.50375)],
        color=outline,
        linewidth=2,
        scalex=False,
        scaley=False,
    )

    # 7 m lines
    ax.plot(
        [xmin + (x_range * 0.175), xmin + (x_range * 0.175)],
        [ymin + (y_range * 0.475), ymin + (y_range * 0.525)],
        color=innerline,
        linewidth=1,
        scalex=False,
        scaley=False,
    )
    ax.plot(
        [xmax - (x_range * 0.175), xmax - (x_range * 0.175)],
        [ymin + (y_range * 0.475), ymin + (y_range * 0.525)],
        color=innerline,
        linewidth=1,
        scalex=False,
        scaley=False,
    )

    # goals
    ax.plot(
        [xmin + (x_range * 0.005), xmin + (x_range * 0.005)],
        [ymin + (y_range * 0.425), ymin + (y_range * 0.575)],
        color=innerline,
        linewidth=1,
        scalex=False,
        scaley=False,
    )
    ax.plot(
        [xmax - (x_range * 0.005), xmax - (x_range * 0.005)],
        [ymin + (y_range * 0.425), ymin + (y_range * 0.575)],
        color=innerline,
        linewidth=1,
        scalex=False,
        scaley=False,
    )

    # remove labels and ticks

    # ax.xaxis.set_major_locator(matplotlib.ticker.NullLocator())
    # ax.yaxis.set_major_locator(matplotlib.ticker.NullLocator())
    # ax.set_xticklabels([])
    # ax.set_yticklabels([])
    fig.subplots_adjust(bottom=0.0, top=1.0, left=0.0, right=1.0)
    # plt.xlim(right=xmax/2)
    if show:
        plt.show()

    return fig, ax


class AnimPlotterHandball:
    def __init__(
        self,
        pos_dict,
        num_frames,
        pos_sets_scatter_kwargs={
            "balls": {"c": "k", "s": 200, "zorder": 1000},
            "team_a": {"c": "r", "s": 400, "zorder": 100},
            "team_b": {"c": "b", "s": 400, "zorder": 100},
        },
        figsize=(10, 5),
    ) -> None:

        self.pos_dict = pos_dict
        self.num_frames = num_frames
        self._fig, self._ax = plot_handball_pitch(
            xmin=0, xmax=40, ymin=0, ymax=20, figsize=figsize, show=False
        )

        self._fnc_scatter_dict = {
            pos_set: self._ax.scatter([], [], **pos_sets_scatter_kwargs[pos_set])
            for pos_set in pos_dict.keys()
        }

    def save(self, fout: Path):
        def _update_figure(frame_number, *fargs):
            for pos_set, xyz in self.pos_dict.items():
                self._fnc_scatter_dict[pos_set].set_offsets(
                    xyz[frame_number, :, :2]
                )  # (num_pos, 2)

        anim = animation.FuncAnimation(
            self._fig,
            func=_update_figure,
            frames=self.num_frames,
            interval=1,
            repeat=False,
        )
        writervideo = animation.FFMpegWriter(fps=30, extra_args=["-vcodec", "libx264"])

        pbar = tqdm(total=self.num_frames, miniters=50)
        anim.save(
            fout, writer=writervideo, progress_callback=lambda _, __: pbar.update()
        )

    def animate(self, fps=30, repeat=True):
        def _update_figure(frame_number, *fargs):
            for pos_set, xyz in self.pos_dict.items():
                self._fnc_scatter_dict[pos_set].set_offsets(
                    xyz[frame_number, :, :2]
                )  # (num_pos, 2)

        anim = animation.FuncAnimation(
            self._fig,
            func=_update_figure,
            frames=self.num_frames,
            interval=int(1 / fps * 1000),
            repeat=repeat,
        )
        return anim

