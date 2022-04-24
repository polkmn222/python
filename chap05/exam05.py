# 패키지

import game.sound.echo
game.sound.echo.echo_test()

from game.sound import echo
echo.echo_test()

from game.sound.echo import echo_test
echo_test()

"""
import game
game.sound.echo.echo_test()
import game.sound.echo.echo_test
"""

"""
from game.sound import *
echo.echo_test()
"""

from game.sound import *
echo.echo_test()

"""
나혼자 코딩
*을 사용하여 render.py 파일 안의 render_test 함수를 사용해 보시요.
"""
from game.graphic import *
render.render_test()

from game.graphic.render import render_test 
render_test()


