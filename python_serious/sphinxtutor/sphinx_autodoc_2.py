"""
이 모듈은?
----------
이 모듈은 문서화 테스트를 위한 두 번째 모듈입니다.

Revision History
-----------------
 * [2022/04/10] - 예제 모듈 작성    
"""
import warnings

class TwicePrint(object):
    """문자열을 받아 두 번 출력하는 클래스
    
    :param str s: s 문자열
    """

    def __init__(self, s):
        self._s = s


    def twice_print(self):
        """미리 입력받은 문자열 s를 두 번 출력한다.

        예제:

            >>> TwicePrint('Hello, Sphinx').twice_print()
            'Hello, Sphinx Hello, Sphinx'
        
        :returns str: ``s + ' ' + s``
        """
        return self._s + ' ' + self._s


class Car(object):
    """API 변경사항 문서화하기 예제
    """

    def turn_left(self):
        """Turn the car left

        .. deprecated:: 0.0.1
        Use :func:`turn` instead with the direction argument set to left        
        """    
        warnings.warn('turn_left is deprecated; use turn instead', DeprecationWarning)
        self.turn(direction='left')

    def turn(self, direction):
        """Turn the car in some direction
        
        :param direction: The direction to turn to
        :type direction: str
        """

        print(f'turn {direction}')
     