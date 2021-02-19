
I couldn't find an automated interior designer artificial intelligence solution, so I decided to experiment and try using generative adversarial neural networks.

For my [supercar design concept Aria Dio](https://www.facebook.com/TheAriaDio), I had already modeled the interior manually in Rhino3d 7, but I was interested to see how well ai would tackle the task. I am reporting these early results of my initial trial in this github repository.

I expect more training time to generate higher resolution interiors, instead of the current somewhat hyper-artlike result.


Interior imagined after 0 epochs:
![Alt Text](https://github.com/JordanMicahBennett/WORLDS-FIRST-OPEN-SOURCE-AI-CAR-INTERIOR-DESIGNER/blob/main/showcase/imagined_interior_0_epochs.png?raw=true)

Interior imagined after 200 epochs:
![Alt Text](https://github.com/JordanMicahBennett/WORLDS-FIRST-OPEN-SOURCE-AI-CAR-INTERIOR-DESIGNER/blob/main/showcase/imagined_interior_200_epochs.png?raw=true)

Interior imagined after 2000 epochs:
![Alt Text](https://github.com/JordanMicahBennett/WORLDS-FIRST-OPEN-SOURCE-AI-CAR-INTERIOR-DESIGNER/blob/main/showcase/imagined_interior_2000_epochs.png?raw=true)

Interior imagined after 9000 epochs:
![Alt Text](https://github.com/JordanMicahBennett/WORLDS-FIRST-OPEN-SOURCE-AI-CAR-INTERIOR-DESIGNER/blob/main/showcase/imagined_interior_9000_epochs.png?raw=true)



#Project mechanism:

Given dataset of "fake" car interiors, as well as real car interiors, a generative adversarial neural network is trained for 9000 epochs to reasonably learn what real car interiors look like, by learning to construct them from this dataset pair of fakes/reals.





#Project workflow:

1. Collect a dataset of real interiors. 
	* Interiors downloaded using python api, [bing image downloader](https://github.com/gurugaurav/bing_image_downloader).
	
	* If you want to make a dataset of your own, and you run into issues with the original usage instructions, use [God's simple fix](god_invoke_image_downloader) which just does what another author suggested [in the issues section of the same page](https://github.com/gurugaurav/bing_image_downloader/issues/4). 
	
2. Create a dataset of "fake" car interiors. 

	* If you want to make a dataset of your own, use [my modified version of a sketchify utility](god_batch_sketchify_utility), which I converted to do batch conversion from a directory of color pics to sketched versions, based on [this author's code](https://github.com/rra94/sketchify/blob/master/sketchify.ipynb) that did the same thing but for single images.
	
3. Train a GAN on this dataset.

	* If you want to train your own, see [my quick instructions](god_training_instructions.md).

Whether this workflow is the most optimal path is unknown.
