using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Cinemachine;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    [SerializeField] CharacterController2D playerControllScpt;
    [SerializeField] PlayerMovement playerMoveScpt;

    [SerializeField] BoxCollider2D playerBox;
    [SerializeField] CircleCollider2D playerCir;

    [SerializeField] Rigidbody2D playerRigid;
    [SerializeField] Vector2 DeathForce;

    [SerializeField] CinemachineVirtualCamera mainCam;
    
    [Header("WinGame")]
    [Space]
    [SerializeField] GameObject winCanvas;


    [Header("GameOver")]
    [Space]
    [SerializeField] GameObject gameOverCanvas;
    [SerializeField] float gameOverWaitTime;

    public IEnumerator GameOver()
    {
        mainCam.m_Follow = null;

        playerControllScpt.enabled = false;
        playerMoveScpt.enabled = false;

        playerBox.isTrigger = true;
        playerCir.isTrigger = true;

        playerRigid.AddForce(DeathForce, ForceMode2D.Impulse);

        yield return new WaitForSeconds(gameOverWaitTime);
        gameOverCanvas.SetActive(true);

    }
    public void WinLevel()
    {

        playerControllScpt.enabled = false;
        playerMoveScpt.enabled = false;

        winCanvas.SetActive(true);

    }

    public void LoadScene(int SceneId)
    {
        SceneManager.LoadScene(SceneId);
    }

}
