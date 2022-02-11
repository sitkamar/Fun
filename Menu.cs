using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class Menu : MonoBehaviour {
    public void PlayGame()
    {
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex + 1);
    }
    public void QuitGame()
    {
        Debug.Log("Quit");
        Application.Quit();2022-01-24 13:46:42: alt_l
	alt_l
2022-01-24 13:46:43: tab
	tab
2022-01-24 13:46:43: alt_l
	alt_l
2022-01-24 13:46:44: alt_l
	alt_l
2022-01-24 13:46:44: caps_lock
	caps_lock
2022-01-24 13:46:46: alt_l
	alt_l
2022-01-24 13:46:47: caps_lock
	caps_lock
2022-01-24 13:46:47: d
	d
2022-01-24 13:46:48: a
	a
2022-01-24 13:46:48: s
	s
2022-01-24 13:46:48: d
	d
2022-01-24 13:46:48: f
	f
2022-01-24 13:46:56: backspace
	backspace
2022-01-24 13:47:06: backspace
	backspace
2022-01-24 13:47:08: ctrl_l
	ctrl_l
2022-01-24 13:47:08: 
	
2022-01-24 13:47:18: ctrl_l
	ctrl_l
2022-01-24 13:47:18: 
	
2022-01-24 13:47:18: ctrl_l
	ctrl_l
2022-01-24 13:47:19: 
	
2022-01-24 13:47:20: 
	

    }
}