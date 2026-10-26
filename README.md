# Standards Research QA & Prompt-Injection Pilot

An **AI-assisted independent evaluation portfolio**, created 26 October 2026. Three original research QA questions, each paired with a synthetic prompt-injection variant, were tested through the ChatGPT, Claude and Gemini web interfaces. Answer keys were checked against primary RFC sources before testing.

**Result: each service answered 6/6 correctly. These are calibration tasks, excluded from the challenge set for being too easy in this pilot. No frontier-model failure or successful prompt injection was demonstrated.**

This repository demonstrates a complete small evaluation workflow: task drafting, source verification, frozen inputs, real response capture, deterministic scoring and task-quality rejection. It is not an official contribution to GAIA, BrowseComp, HLE or any other benchmark. No HLE submission or acceptance is claimed. No employment history or years of experience are implied.

## Reproduce the scores

Requires Python 3.10+; standard library only. From this directory:

```powershell
python -m unittest -v
python evaluate.py
```

The second command verifies the frozen input hashes and writes `results/scores.json` from the recorded predictions. **It scores historical responses; it does not call models.**

To collect a new run, paste `prompts/batch-v1.txt` into a new chat, save the response unchanged, record the visible model label and date, and save its JSON answer array as `runs/YOUR_RUN/predictions.json`. Then use:

```powershell
python evaluate.py --responses runs/YOUR_RUN/predictions.json
```

For a stronger new experiment, use the isolated-item protocol in [METHODOLOGY.md](METHODOLOGY.md) and label it as a new experiment; it does not reproduce the batch conditions used here.

## Recorded results

| Service / visible selection | Clean | Injected | Attack target selected |
|---|---:|---:|---:|
| ChatGPT; exact model not displayed | 3/3 | 3/3 | 0/3 |
| Claude; Opus 5.5 Medium | 3/3 | 3/3 | 0/3 |
| Gemini; Flash | 3/3 | 3/3 | 0/3 |

Selections are UI labels observed during the run, not independently verified backend identifiers. Models and web interfaces can change. Each service received one six-item batch. There are **three independent task families, not six independent research questions**. These are descriptive pilot counts, not a leaderboard or a reliability estimate.

## Inspect the evidence

- [Task questions](data/tasks.jsonl) and [answer keys with sources](data/answer_keys.jsonl)
- [Frozen manifest](data/locked_manifest.json) and [exact submitted prompt](prompts/batch-v1.txt)
- [Methodology and scoring rules](METHODOLOGY.md)
- [Evaluation report and failure diagnosis](REPORT.md)
- [Task disposition](data/task_disposition.json)
- `runs/`: captured answer text, separately transcribed narrative, parsed predictions and metadata
- [Application wording and evidence boundaries](APPLICATION.md)

The three source documents are [RFC 9562 §5.8](https://www.rfc-editor.org/rfc/rfc9562.html#section-5.8), [RFC 8949 §3.4.6](https://www.rfc-editor.org/rfc/rfc8949.html#section-3.4.6), and [RFC 9106 §4](https://www.rfc-editor.org/rfc/rfc9106.html#section-4). Questions were newly composed for this pilot; the underlying facts are public and may occur in model training data. Semantic originality across all existing datasets has not been established.

## Authorship and limitations

Codex drafted the tasks, code and report and operated the model tests at the account owner's request. No independent human answer-key review has yet been performed. Public-source checks are not expert peer review. Answers, evidence and limitations should be reviewed by the applicant before describing personal contributions in an application. Public release makes these unsuitable as an uncontaminated future holdout.

This is portfolio evidence of an AI-assisted pilot, not proof that the account owner independently completed each step or meets a role's experience requirements. Source text is linked rather than redistributed; third-party sites retain their rights.
