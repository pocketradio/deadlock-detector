# Distributed deadlock detection system

![WIP](https://img.shields.io/badge/status-WIP-orange)

## Status

Core detection and streaming pipeline is complete.  
UI and WebSocket-based visualization are intentionally deferred for now and will be integrated later.

---

## About

A simulation-based deadlock detection system that models process–resource interactions, constructs a Wait-For Graph, and detects deadlocks using Tarjan’s Strongly Connected Components (SCC) algorithm.

System state and detection events are streamed using Apache Kafka.

This project focuses on distributed detection logic and event-driven design.

---

## What it does

- Simulates processes requesting and releasing resources
- Builds a Wait-For Graph from live system state
- Detects deadlocks via Tarjan's SCC
- Streams graph updates and deadlock events through Kafka
- Supports multiple independent simulations via keyed streams

---
