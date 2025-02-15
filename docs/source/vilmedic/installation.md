# Installation


<div class="info_box">
	<b>ViLMedic</b> is built on top of important packages:<br/>
- python>=3.9<br/>
- <a href="http://pytorch.org/">pytorch 1.8.1</a><br/>
- <a href="https://huggingface.co/transformers/">transformers 4.5.1</a><br/>
	<div class="highlight">
<pre>conda create --name vilmedic python==3.9 -y
</pre></div>	
</div>


<center><b>There is two ways of installing ViLMedic, please read until the end:</b></center><br/>

If you plan to use the model-zoo only, you can install vilmedic using pip:
```bash
pip install vilmedic
```

If you want to initiate trainings or replicate solutions, install ViLMedic in development mode:
```bash
git clone https://github.com/jbdel/vilmedic
python setup.py develop
```


<div class="warning_box">
	<b>In any case</b>, please download the extra resources (required for scoring and more) by typing this command
	in the terminal:
	<div class="highlight">
<pre>vilmedic-install-extra</pre></div>	
</div>

ViLMedic is structured as follows:
```
|-- vilmedic
	|-- data
	|-- bin
	|-- config
	|-- vilmedic
	|  |-- datasets
	|  |-- executors
	|  |-- networks
	|  |  |  |-- blocks
	|  |  |  |-- models
	|  |-- scorers
```

All pretrained models and datasets downloaded from this documentation will be placed in the `data` folder.