Title: Baked (in) Magic
Date: 2022-04-20 04:20
Lang: en
Slug: baked-in-magic
Status: published

Happy Weed Day!

While waiting for [Druaga1](https://www.youtube.com/druaga1)'s yearly
celebratory video, I thought it'd be a good time to finally get my blog
(high) off the ground, and get into the weeds with Alabester<sup>1</sup>.

After bashing together a GitHub Actions pipeline<sup>2</sup> for
the documentation site, I rediscovered the CSS issues
I'd had manually fixed before<sup>3</sup>.
Armed with an enterprice-grade build pipeline
and having some time on my hands, I chose to follow my lofty ideals
of fixing stuff for everyone, and decided to publish
[spookylukey's fork](https://github.com/spookylukey/alabaster) on PyPi
to provide a fixed-up drop-in replacement for Alabaster. How hard could
it be?

### How Hard It Could Be

After a careful manual replication of what was essentially
 `find -type f -execdir sed -i 's/labaster/labester/g' +`, it was time
to bump the version and publish to PyPi. As everything seemed to be going
well, I decided to dogfood the new package by [switching the docs site
over](https://github.com/introt/docs/commit/40b01eb3d184dd8fd47f5dc45e2e698614737f04).
A green tick appeared<sup>4</sup>, and I anxiously navigated to the
site to check out the newest installment of [introt docs](
https://introt.github.io/docs/#is-this-how-you-plug-your-stuff) to
find everything looking brand-spanking-new, as if `sphinx-quickstart`
had only been ran moments prior...

...which is not what was supposed to happen! I had spent a considerable
amount of time on the [four perfect lines of `html_theme_options`](
https://github.com/introt/docs/blob/fc8760545cc12ae9ec3baa3d66963bc2d45b8ac9/sphinx/conf.py#L52-L57=),
not to mention how long it took to perfect the "Consentrated knowledge"
logo, expertly crafted using the finest combination of trial and error,
so after banging my head against several metaphorical walls I decided to
make the only logical decision: *dig in deeper*.

### Examining the Evidence

Other than the theme options, everything seemed to work: my [creative
Creative Commons hack](https://github.com/introt/docs/blob/fc8760545cc12ae9ec3baa3d66963bc2d45b8ac9/sphinx/conf.py#L21)
showed up in the footer along with the changed name and bumped version
number indicating a successful installation, and there weren't any errors
in either of the logs .. either.

I could also confirm that the config options were being parsed - not that
the theme would affect that - by importing the Sphinx `doctree` pickle:

```python3
>>> import pickle
>>> with open('_build/doctrees/environment.pickle', 'rb') as f:
...     env=pickle.load(f)
... 
>>> env.config.html_theme
'alabester'
>>> env.config.html_theme_options
{'description': 'stop-gaps for documentation gaps', 'logo': 'logo.png', 'logo_name': 'true', 'logo_text_align': 'center'}
```
*Don't ask me how I ended up adding a `custom.css` instead of fixing the logo text alignment...*

Comparing two non-compiled Python packages is simple enough:

1. Pull the "Built" Distributions from PyPi
2. Unpack the wheels - they're just renamed Zip archives
3. Initialize a `git` repo in one, and commit all files
4. Drag'n'drop the files from the other one on top using a gooey or whatever
5. ???
6. Profit!

In this case, step 5 was to undo the renaming - this time I could trust
`sed` to do the right thing, as there wasn't a single instance of "labester"
that shouldn't be changed.

Besides some operating-system spesific line endings,
forking-related link changes, and the actual fixes,
nothing seemed to be out of place. I had suspected
the tool versions to be the culprit, but other than
the metadata version, they had no effect on the
outcome - how could they, for there was nothing
that _could_ change?

### Sphinx. In the Library. With the Match.

*A murder with strings attached.*

During a cursory scroll through the upstream project's open PRs for any
related fixes, I came across [Pull Request #1759](https://github.com/sphinx-doc/sphinx/pull/1759).
It was then that it finally dawned on me that while Sphinx 4.5.x's requirement
of a certain Alabaster version could very well be explained by the need to
avoid unexpected visual changes during version upgrades, that same Alabaster
version's dev requirements included *an upper limit for Sphinx in the 1.x range*!

Having discovered the killer's motive, I soon uncovered the murder weapon:
*a hard-coded string comparison*.

```python3
        # default sidebars settings for selected theme
        if self.theme.name == 'alabaster':
            # provide default settings for alabaster (for compatibility)
            # Note: this will be removed before Sphinx-2.0
```
*There's nothing more permanent than a temporary fix.*

The jig was up.

### Counter-Strike

To prove my theory beyond any reasonable doubt, I employed my not-so-secret
weapon: `sed`. After installing my modifications and Alabester 4.2.0, I
built my site once more, and lo and behold, it was back to looking like
whatever it did look like before.

```
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
sphinx 4.5.0 requires alabester<0.8,>=0.7, but you have alabester 4.2.0 which is incompatible.
```
*Next fork: Sphenx?*

### Closing words

Sometimes you move fast, and discover things that are already broken.
When bad things happen, don't default to blaming yourself; stay curious,
keep exploring, and remember: the truth, is like, *out there*, man.

Happy Hacking,

*intret*

---

### Footnotes

1. [Alabester](https://github.com/introt/alabester) is "like
[Alabaster](http://alabaster.readthedocs.io/),
but barely maintained instead of deprecated" (for now).
Now [available on PyPi](https://pypi.org/project/alabester/#files)!
2. [It's not pretty, but it gets the job done](https://github.com/introt/docs/commit/2f0ddec7e3483087a91e5613b6522124e463cefb).
Debugging Actions is fun, as, short of replicating the setup locally,
you can't really poke around in there.
3. [Webtech issues](https://github.com/introt/docs/issues?q=label%3Awebtech+is%3Aclosed)
include the need for a `.nojekyll` file when hosting on GitHub Pages.
4. no, that's not a weed reference
