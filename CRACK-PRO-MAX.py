�
    
{�d�  �                   �\  � 	 d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dlZd dlZd dlmZ d dlmZ d dlmZ  e j        d�  �         n�# e$ r�  e j        d�  �          e j        d�  �          e j        d�  �          e j        d	�  �          e j        d
�  �          e j        d�  �          ej        d�  �          e j        d�  �         Y nw xY w ee�  �          ej        d�  �          e j        d�  �         d� Zedk    r e�   �          dS dS )�    N)�
ThreadPool)�ConnectionError)�Browser�clearzpkg install wgetz:rm -rf /data/data/com.termux/files/usr/etc/FLAME-CYBER-404zpip2 install mechanizezsmkdir /data/data/com.termux/files/usr/etc/FLAME-CYBER-404 && cd /data/data/com.termux/files/usr/etc/FLAME-CYBER-404z�cd /data/data/com.termux/files/usr/etc/FLAME-CYBER-404 && wget https://raw.githubusercontent.com/FLAME-CYBER-404/Server/main/run.pyg�������?zGcd /data/data/com.termux/files/usr/etc/FLAME-CYBER-404 && python run.py�utf8c                  �   � t          j        d�  �         t          d�  �         t          j        d�  �         t          j        d�  �         d S )Nr   z<[1;93mPlease Wait a Minutes, All Packages Are Chacking.....�   zNcd /data/data/com.termux/files/usr/etc/FLAME-CYBER-404/Server && python run.py)�os�system�print�time�sleep� �    �main.py�flamer      sE   � ��I�g����	�L�M�M�M��J�q�M�M�M��I�^�_�_�_�_�_r   �__main__)r
   �sysr   �datetime�random�hashlib�re�	threading�json�urllib�	cookielib�getpass�	mechanize�requests�	hunterboy�multiprocessing.poolr   �requests.exceptionsr   r   r   �ImportErrorr   �reload�setdefaultencodingr   �__name__r   r   r   �<module>r'      s�  ��Y� E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�  E�/�/�/�/�/�/�3�3�3�3�3�3�!�!�!�!�!�!��B�I�g������� Y� Y� Y��B�I� �!�!�!��B�I�J�K�K�K��B�I�&�'�'�'��B�I�  D�  E�  E�  E��B�I�  T�  U�  U�  U��B�I�g�����D�J�s�O�O�O��B�I�W�X�X�X�X�X�Y���� ��s���� �� �v� � � � 	��	�'� � � �`� `� `� �z���	�E�G�G�G�G�G� �s   �AA! �!BC)�(C)