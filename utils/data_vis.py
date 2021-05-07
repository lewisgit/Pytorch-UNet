import matplotlib.pyplot as plt


def plot_img_and_mask(img, mask, full_mask):
    classes = mask.shape[2] if len(mask.shape) > 2 else 1
    fig, ax = plt.subplots(1, classes * 2 + 1)
    ax[0].set_title('Input image')
    ax[0].imshow(img)
    if classes > 1:
        for i in range(classes):
            ax[2*i+1].set_title(f'Output mask (class {i+1})')
            ax[2*i+1].imshow(mask[:, :, i])
            ax[2*i+2].set_title(f'Full mask mask (class {i+1})')
            ax[2*i+2].imshow(full_mask[:, :, i])
    else:
        ax[1].set_title(f'Output mask')
        ax[1].imshow(mask)
        ax[2].set_title(f'Full mask')
        ax[2].imshow(full_mask)
    plt.xticks([]), plt.yticks([])
    plt.show()
