#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms

## resource links
## https://newafrikan77.files.wordpress.com/2016/12/img_1101.jpg
## https://newafrikan77.wordpress.com/2016/12/16/ugwuele-the-ancient-shrine-of-isi-ume-the-origin-of-humankind-igbo-and-the-worship-of-the-great-mother-nnem-chukwu/
## https://www.imodara.com/discover/nigeria-igbo-alusi-spirit-force-figure/


rooms = {

    'Hall' : {
            'south' : 'south_wing',
            'west'  : 'secret_doorway',
            'east' : 'east_wing',
            'item'  : 'key',
            'desc'  : 'It is a rainy foggy day in the Sacred Grove of Ihu Nne. You are standing in the great hall of Mbari, Great Mother Goddess Alusi Ala\'s shrine. On the wall, there is a  \n' 
            'painted figure of Ala, where she balances a child on her knees while she brandishes a sword and is surrounded by the images of other deities, humans and animals. You are Ishindu,\n'
            'the priest and clergy of Ala and your mision is avert an apocalyspe by finding and sealing the terrifying masqurade Ekwensu in a golden orb-jar-thingamajiga. To your south is the south wing and to your west is a \n' 
            'secret doorway. You look under the painting and you find a key.'
        },

    'south_wing' : {
            'north' : 'Hall',
            'item'  : ['map', 'lantern'],
            'desc' : 'You are in the south_wing. There is a large map of the shrine on the wall'
        },

    'secret_doorway' : {
            'north' : 'Hall',
            'item'  : 'telepotion',
            'desc' : 'you suddenly find yourself in a crypt. '
        },

    'east_wing' : {
            'west' : 'Hall',
            'south' : 'grove_mouth',
            'monster'  : 'Ekwensu',
            'desc' : 'you are in the east wing. be at alert, Ekwensu lurks nearby'
        },
    'grove_mouth' : {
            'north' : 'east_wing',
            'desc' : 'Great work warrior, you have found your way out of the Grove'

        }
}    