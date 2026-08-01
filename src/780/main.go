package main

import (
	"errors"
	"fmt"
	"sync"
)

type Account struct {
	ID      string
	Balance float64
	mu      sync.Mutex
}

type transaction struct {
	from, to string
	amount   float64
}

var wg sync.WaitGroup

func main() {
	accounts := []*Account{
		{ID: "A", Balance: 100},
		{ID: "B", Balance: 200},
		{ID: "C", Balance: 0},
	}

	transactions := []transaction{
		{"A", "B", 50},
		{"B", "C", 300},
		{"A", "C", 10},
		{"B", "C", -10},
	}

	for _, tx := range transactions {
		wg.Add(1)
		// go processTrx()
		go func(tx transaction) {
			defer wg.Done()

			fromAcc := findAccount(accounts, tx.from)
			toAcc := findAccount(accounts, tx.to)

			if fromAcc == nil || toAcc == nil {
				fmt.Println("Invalid account")
				return
			}

			if err := Transfer(fromAcc, toAcc, tx.amount); err != nil {
				fmt.Print(err)
			}
			fmt.Println("success")

		}(tx)
		wg.Wait()
		for _, a := range accounts {
			fmt.Println(a.ID, a.Balance)
		}
	}
}

func Transfer(from, to *Account, amount float64) error {
	if amount <= 0 {
		return errors.New("Invalid amount")
	}

	unlock := lockAccouns(from, to)
	defer unlock()

	if from.Balance < amount {
		return fmt.Errorf("Invalid balance")
	}
	from.Balance -= amount
	to.Balance += amount

	return nil
}

func lockAccouns(a, b *Account) func() {
	if a.ID < b.ID {
		a.mu.Lock()
		b.mu.Lock()
		return func() {
			b.mu.Unlock()
			a.mu.Unlock()
		}
	}
	a.mu.Lock()
	b.mu.Lock()
	return func() {
		b.mu.Unlock()
		a.mu.Unlock()
	}
}

func findAccount(accs []*Account, id string) *Account {
	for i := range accs {
		if accs[i].ID == id {
			return accs[i]
		}
	}
	return nil
}
